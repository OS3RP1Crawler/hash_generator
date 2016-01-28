#!/usr/bin/python

import random

class Generator():

    def __init__(self, base, length, amount, encode, decode):
        '''Base to generate in, the length of the hashes, amount of hashes to generate, conversion function'''
        self.base = base
        self.length = length
        self.amount = amount
        self.encode = encode
        self.decode = decode
        self.i = 0
        self.lowerBound = 0
        self.upperBound = pow(self.base, self.length)

    def getRandomNumber(self):
        return random.randint(self.lowerBound, self.upperBound)

    def getShortHash(self):
        n = self.getRandomNumber()
        enc = self.encode(n)
        return self.pad(enc)

    def pad(self, n):
        if len(n) < self.length:
            x = self.length - len(n)
            return ('0' * x) + n
        else:
            return n

    def __iter__(self):
        return self

    def next(self):
        if self.i >= self.amount:
            raise StopIteration
        else:
            self.i += 1
            return self.getShortHash()
