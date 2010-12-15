#!/usr/bin/env python
#
# PyPass - Python Random Password Generator
#
# Author - Honza Pokorny <me@honza.ca>
# (c) 2010 - Licensed under GPLv3

import random
import string
import sys


class PyPass(object):
    """
    PyPass Strong Password Generator
    It makes sure no character is repeated. By default, it includes uppercase,
    lowercase, numbers, and punctuation. Lowercase and uppercase are treated as
    separate types (you could have K and k in one password).
    """

    LOWER = string.lowercase
    UPPER = string.uppercase
    SPECIAL = string.punctuation

    def __init__(self, length=8):
        self.length = length
        self.last = 1
        self._upper = []
        self._lower = []
        self._numbers = []
        self._special = []

    def _get_lower(self):
        a = self.LOWER[random.randint(1, len(self.LOWER) - 1)]
        while True:
            a = self.LOWER[random.randint(1, len(self.LOWER) - 1)]
            if a not in self._lower:
                break
        self._lower.append(a)
        self.last = 1
        return a

    def _get_upper(self):
        a = self.UPPER[random.randint(1, len(self.UPPER) - 1)]
        while True:
            a = self.UPPER[random.randint(1, len(self.UPPER) - 1)]
            if a not in self._upper:
                break
        self._upper.append(a)
        self.last = 2
        return a

    def _get_number(self):
        a = random.randint(1, 10)
        while True:
            a = random.randint(1, 10)
            if a not in self._numbers:
                break
        self._numbers.append(a)
        self.last = 3
        return str(a)

    def _get_special(self):
        a = self.SPECIAL[random.randint(1, len(self.SPECIAL) - 1)]
        while True:
            a = self.SPECIAL[random.randint(1, len(self.SPECIAL) - 1)]
            if a not in self._special:
                break
        self._special.append(a)
        self.last = 4
        return a

    def _get_next(self):
        i = 0
        while True:
            i = random.randint(1, 4)
            if i != self.last:
                break
        if i == 1:
            return self._get_lower()
        elif i == 2:
            return self._get_upper()
        elif i == 3:
            return self._get_number()
        elif i == 4:
            return self._get_special()
        else:
            pass

    def _reset(self):
        """
        Reset lists of used characters. Used when generating multiple passwords
        """
        self._special = []
        self._lower = []
        self._upper = []
        self._numbers = []

    def run(self):
        self._reset()
        s = ""
        self.last = ""
        for a in range(0, self.length):
            s += self._get_next()
        return s


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
        if arg == '-h':
            print 'Usage:'
            print 'python main.py       (one 8-char long password)'
            print 'python main.py 12    (one 12-char long passwords)'
            print 'python main.py 12 10 (ten 12-char long passwords)'
            sys.exit(0)
        pypass = PyPass(int(arg))
    except IndexError:
        pypass = PyPass()
    try:
        arg = int(sys.argv[2])
    except IndexError:
        arg = 1
    for x in range(0, arg):
        print pypass.run()
