#!/usr/bin/python

from urlgenerator_errors import FileCreationError, NoSuchPathError, NoSuchHandleError
import os
import traceback

class FileWriter():
    def __init__(self, path, base, alphabet, amount):
        if not path.endswith('/'):
            path += "/"

        self.path = path
        self.base = base
        self.noFiles = len(alphabet)
        self.fileHandles = {}
        self.alphabet = alphabet
        self.amount = amount
        self.counter = 0

        if not os.path.exists(path):
            raise NoSuchPathError

    def _createHandle(self, s, mode):
        return open(self.path + s, mode)

    def createFiles(self):
        try:
            for i in range(0, self.amount):
                self.fileHandles[i] = self._createHandle(str(i), "w+")
        except Exception, e:
            print e
            raise FileCreationError

    def closeFiles(self):
        for key, f in self.fileHandles.iteritems():
            f.close()

    def write(self, shortHash):
        self.counter = (self.counter + 1) % self.amount
        try:
            handle = self.fileHandles[self.counter]
            handle.write(shortHash + "\n")
        except Exception:
            raise NoSuchHandleError

    def __enter__(self):
        self.createFiles()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeFiles()
