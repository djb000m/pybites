#!/usr/bin/env python


class Person:
    def __repr__(self):
        return Person()

    def __str__(self):
        return "I am a person"


class Father(Person):
    def __repr__(self):
        return Father()

    def __str__(self):
        return f"{super().__str__()} and cool daddy"


class Mother(Person):
    def __repr__(self):
        return Mother()

    def __str__(self):
        return f"{super().__str__()} and awesome mom"


class Child(Father, Mother):
    def __repr__(self):
        return Child()

    def __str__(self):
        return "I am the coolest kid"
