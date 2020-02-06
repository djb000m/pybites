#!/usr/bin/env python

import itertools


class Animal:

    # Static/Class Variables
    # iterating variable counting from 10001
    __seq = itertools.count(10001)
    # list of all Animal instances
    __zoo = []

    def __init__(self, animal_input):
        # set Instance Variables for name and id
        self.__name = animal_input.title()
        self.__id = next(self.__seq)
        # Append this instance to the Class __zoo variable
        self.__zoo.append(self)

    # returns '10001. Animal'
    def __str__(self):
        return f"{self.id}. {self.name}"

    # property getters and setters - good practice for each instance
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, animal_input):
        self.__name = animal_input

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_input):
        self.__id = id_input

    # class method to supply list of all Animal instances created
    @classmethod
    def zoo(cls):
        return "\n".join([str(animal) for animal in cls.__zoo])


dog = Animal("dog")
cat = Animal("cat")
fish = Animal("fish")
lion = Animal("lion")
mouse = Animal("mouse")
print(Animal.zoo())
horse = Animal("horse")
print(str(horse))
horse = Animal("monkey")
print(str(horse))
