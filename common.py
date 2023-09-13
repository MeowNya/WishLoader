#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'MeowNya'


from config import DIR_LOGS
from third_party.mywishlist_ru.common import get_logger


log = get_logger(__file__, file=DIR_LOGS / "log.txt")
