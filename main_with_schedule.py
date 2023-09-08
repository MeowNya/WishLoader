#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import time

import schedule

from main import main as run, log


schedule.every().day.at("04:20").do(run)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)

    except Exception:
        log.exception("Ошибка:")
        time.sleep(60)
