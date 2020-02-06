#!/usr/bin/env python

import collections.abc

# from time import strftime ## not needed?

MSG = "Hey {}, there are more people with your birthday!"

## Subclassing built-in objects like dict is a bad idea, apparently
## Python provides these AbstractBaseClasses (abc) that provide a bunch of functionality
## and behave like the base class.
## The below is the minimum to run a dict-like subclass - note the custom code in __setitem__
class BirthdayDict(collections.abc.MutableMapping):
    """A dictionary that prints a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, name):
        return self.store[name]

    def __setitem__(self, name, birthday):
        if any(
            birthday.strftime("%d/%m") == dt.strftime("%d/%m")
            for dt in self.store.values()
        ):
            print(f"Hey {name.title()}, there are more people with your birthday!")
        self.store[name] = birthday

    def __delitem__(self, name):
        del self.store[name]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)


## Here's the way pybites does it. It subclasses dict, which apparently is not the recommended way of doing this

# class BirthdayDict(dict):
#     def __init__(self, *args, **kwargs):
#         self.update(*args, **kwargs)

#     def __setitem__(self, name, birthday):
#         has_birthday = any(
#             birthday.strftime("%d/%m") == dt.strftime("%d/%m") for dt in self.values()
#         )

#         if has_birthday:
#             print(MSG.format(name))
#         super().__setitem__(name, birthday)

