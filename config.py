#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "MeowNya"


import os
import sys

from pathlib import Path


# Current folder where the script is located
DIR = Path(__file__).resolve().parent

DIR_LOGS = DIR / "logs"
DIR_LOGS.mkdir(parents=True, exist_ok=True)

TOKEN_FILE_NAME = DIR / "TOKEN.txt"

try:
    TOKEN = os.environ.get("TOKEN") or TOKEN_FILE_NAME.read_text("utf-8").strip()
    if not TOKEN:
        raise Exception("Токен пустой!")

except:
    print(
        f"Нужно добавить логин и пароль в файл {TOKEN_FILE_NAME.name} или в переменную окружения TOKEN"
    )
    TOKEN_FILE_NAME.touch()
    sys.exit()

LOGIN, PASSWORD = TOKEN.split("/")

if path := os.environ.get("DIR_NEW_WISHES"):
    DIR_NEW_WISHES = Path(path)
else:
    DIR_NEW_WISHES = DIR / "new_wishes"

DIR_NEW_WISHES.mkdir(exist_ok=True, parents=True)

DIR_OK = DIR_NEW_WISHES / "ok"
DIR_OK.mkdir(exist_ok=True, parents=True)

DIR_ERROR = DIR_NEW_WISHES / "error"
DIR_ERROR.mkdir(exist_ok=True, parents=True)
