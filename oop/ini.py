#!/usr/bin/env python

import configparser
import re


class ToxIniParser:
    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.__config = configparser.ConfigParser()
        self.__config.read(ini_file)
        self.__number_of_sections = len(self.__config.sections())

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return self.__number_of_sections

    @number_of_sections.setter
    def number_of_sections(self, value):
        self.__number_of_sections = value

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        envs = self.__config["tox"]["envlist"].strip()
        return [env.strip() for env in re.split(r"\n|,", envs) if env]

        # my original code, nowhere near as elegant as pybites code above...
        #
        # envs = self.__config["tox"]["envlist"].split()
        # envs = [s.strip(",") for s in envs]
        # envs = [s.split(",") for s in envs]

        # flat_list = []
        # for sublist in envs:
        #     for item in sublist:
        #         flat_list.append(item)

        # return flat_list

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        # use a set for list of basepython values.
        # we don't want duplicates and sets automatically drop duplicates = perfect
        py_versions = set()
        for section in self.__config.sections():
            try:
                # see if basepython exists in this section
                py_versions.add(self.__config[section]["basepython"])

            except KeyError:
                # basepython does not exist in this section, carry on
                continue

        return list(py_versions)
