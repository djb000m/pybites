#!/usr/bin/env python

import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join("/tmp", "color_values.py")
urllib.request.urlretrieve("https://bit.ly/2MSuu4z", color_values_module)
sys.path.append("/tmp")

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color=None):
        try:
            self.__rgb = COLOR_NAMES[color.upper()]
            self.__hex = self.rgb2hex(self.__rgb)
            self.__color = color
        except KeyError:
            self.__rgb = None
            self.__hex = None
            self.__color = None

    @property
    def rgb(self):
        return self.__rgb

    @rgb.setter
    def rgb(self, rgb_input):
        self.__rgb = rgb_input

    @property
    def hex(self):
        return self.__hex

    @hex.setter
    def hex(self, hex_input):
        self.__hex = hex_input

    @property
    def name(self):
        return self.__color

    @name.setter
    def name(self, color_input):
        self.__color = color_input

    @classmethod
    def hex2rgb(cls, hex_input):
        """Class method that converts a hex value into an rgb one"""

        # declare an error message
        error_message = f"{hex_input} is not a valid hex value!"

        # check a string has been supplied
        if not isinstance(hex_input, str):
            raise ValueError(error_message)

        # we're only interested in a proper six digit hex color representation (e.g. #000000)
        if not len(hex_input) == 7 or not hex_input.startswith("#"):
            raise ValueError(error_message)

        # handle shortened hex notation - converts to 6 digit notation
        # HOWEVER, pybites don't want this - so commenting out...
        # if len(hex_input) == 4:
        #     hex_input = f"{hex_input[1]*2}{hex_input[2]*2}{hex_input[3]*2}"

        # construct a tuple of ints by iterating through the hex_input string
        return tuple(int(hex_input[i : i + 2], 16) for i in (1, 2, 4))

    @classmethod
    def rgb2hex(cls, rgb_input):
        """Class method that converts an rgb value into a hex one"""
        # define error message
        error_message = f"{rgb_input} is not a valid RGB value!"

        # check that input is a tuple
        if not isinstance(rgb_input, tuple):
            raise ValueError(error_message)

        valid_hex = [1 for n in rgb_input if not (0 <= n < 256)]
        if sum(valid_hex) > 0:
            raise ValueError(error_message)

        # format numbers as hexadecimal - the 02x means 2 digits with 0 for padding and he(x)adeciaml
        # https://stackoverflow.com/questions/14678132/python-hexadecimal#14678150
        return f"#{rgb_input[0]:02x}{rgb_input[1]:02x}{rgb_input[2]:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.__color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        # if slef.rgb has a value, return it.
        # otherwise return "unknown"
        return f"{self.__rgb}" if self.__rgb else "unknown"
