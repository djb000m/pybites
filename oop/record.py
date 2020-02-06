#!/usr/bin/env python


class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self.__high_score = 0

    def __call__(self, new_score=0):
        self.high_score = new_score
        return self.__high_score

    @property
    def high_score(self):
        return self.__high_score

    @high_score.setter
    def high_score(self, new_score):
        if new_score > self.__high_score:
            self.__high_score = new_score
