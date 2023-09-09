#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "MeowNya"


import shutil
from datetime import datetime

from bs4 import BeautifulSoup, Tag

from common import log
from config import LOGIN, PASSWORD, DIR_NEW_WISHES, DIR_OK, DIR_ERROR
from third_party.mywishlist_ru.common import Api, VisibleModeEnum, RatingEnum


def wish_add(wish: Tag, api: Api):
    title = wish.Название.get_text(strip=True)
    img_file_name = wish.Картинка.get_text(strip=True)
    tags = [tag.strip() for tag in wish.Теги.get_text(strip=True).split(",")]
    link = wish.Ссылка.get_text(strip=True)
    price_description = wish.Цена.get_text(strip=True)
    event = wish.Повод.get_text(strip=True)
    notes = wish.Заметка.get_text(strip=True)

    try:
        rating = RatingEnum(
            int(wish.Необходимость.get_text(strip=True))
        )
    except Exception:
        rating = RatingEnum.MEDIUM

    try:
        visible_mode = VisibleModeEnum(
            int(wish.Доступно.get_text(strip=True))
        )
    except Exception:
        visible_mode = VisibleModeEnum.PUBLIC

    wish_id = api.add_wish(
        title=title,
        tags=tags,
        link=link,
        img_path=img_file_name,
        event=event,
        post_current=notes,
        price_description=price_description,
        rating=rating,
        visible_mode=visible_mode,
    )
    log.info(f"Добавлено желание #{wish_id}")


def wish_realise(wish: Tag, api: Api):
    url = wish.Ссылка.get_text(strip=True)
    wish_id = int(url.split("/")[-1])
    thanks = wish.Благодарности.get_text(strip=True)
    api.set_wish_as_granted(wish_id, thanks)
    log.info(f"Желание #{wish_id} исполнено!")


def main():
    log.info("Запуск")
    log.debug(f"{LOGIN}/{PASSWORD}")

    try:
        api = Api(LOGIN, PASSWORD)
        api.auth()

        files = list(DIR_NEW_WISHES.glob("*.xml"))
        log.info(f"Найдено файлов: {len(files)}")

        for file_name in files:
            log.info(f"Чтение {file_name.name!r}")

            soup = BeautifulSoup(open(file_name, "rb"), "xml")

            dir_result = DIR_OK
            try:
                is_ok = False
                if wish := soup.select_one("Желание > Добавить"):
                    wish_add(wish, api)
                    is_ok = True

                if wish := soup.select_one("Желание > Выполнить"):
                    wish_realise(wish, api)
                    is_ok = True

                if not is_ok:
                    raise Exception("Не получилось найти желание для добавления или выполнения")

            except Exception:
                log.exception("Ошибка:")
                dir_result = DIR_ERROR

            now = datetime.now()
            new_file_name = dir_result / f"{now:%Y-%m-%d_%H.%M.%S}_{file_name.name}"
            log.info(f"Перемещение файла в {new_file_name}\n")

            shutil.move(file_name, new_file_name)

    except Exception:
        log.exception("Ошибка:")

    finally:
        log.info("Завершено\n")


if __name__ == '__main__':
    main()
