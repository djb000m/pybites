#!/usr/bin/env python

import secrets

BITES = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
bites_done = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo:
    def __init__(self, bites_done=bites_done):
        self.bites_done = bites_done

    @property
    def available_bites(self):
        return list(BITES.keys() - self.bites_done)

    def _pick_random_bite(self):
        if not self.available_bites:
            raise NoBitesAvailable
        return secrets.choice(self.available_bites)

    def new_bite(self):
        nb = self._pick_random_bite()
        self.bites_done.add(nb)
        return nb


## This is not the way to do this!
## but the list({k: v} bit is interesting and left here for future reference)
# def _pick_random_bite(self):
#     try:
#         return secrets.choice(
#             list(
#                 {k: v for k, v in BITES.items() if k not in self.bites_done}.keys()
#             )
#         )
#     except Exception:
#         raise NoBitesAvailable("No more Bites available, you've done them all!")
