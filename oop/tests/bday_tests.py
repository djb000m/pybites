#!/usr/bin/python

from datetime import date
from time import strftime
from bdaydict import BirthdayDict

bd = BirthdayDict()
bd["bob"] = date(1987, 6, 15)
bd["tim"] = date(1984, 7, 15)
bd["mary"] = date(1987, 6, 15)  # whole date match
bd["sara"] = date(1987, 6, 14)
bd["mike"] = date(1981, 7, 15)  # day + month match

# test = date(1981, 7, 15)

# print(bd["tim"].strftime("%d %m") == bd["mike"].strftime("%d %m"))
# for k, v in bd.items():
#     if test.strftime("%d %m") == v.strftime("%d %m"):
#         print(f"I found me a match, {k}")
