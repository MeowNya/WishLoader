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
        raise Exception("TOKEN is empty!")

except:
    print(
        f"You need to add the bot token to {TOKEN_FILE_NAME.name} or to the TOKEN environment variable"
    )
    TOKEN_FILE_NAME.touch()
    sys.exit()

LOGIN, PASSWORD = TOKEN.split("/")

DIR_NEW_WISHES = DIR / "new_wishes"
DIR_NEW_WISHES.mkdir(exist_ok=True, parents=True)

DIR_OK = DIR_NEW_WISHES / "ok"
DIR_OK.mkdir(exist_ok=True, parents=True)

DIR_ERROR = DIR_NEW_WISHES / "error"
DIR_ERROR.mkdir(exist_ok=True, parents=True)
