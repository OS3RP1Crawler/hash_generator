#!/usr/bin/python


class Error(Exception):
    pass

class InvalidArgument(Error):
    def __init__(self, msg):
        self.msg = msg

class FileCreationError(Error):
    def __init__(self):
        self.msg = "Error in creating files"

class NoSuchHandleError(Error):
    def __init__(self):
        self.msg = "Error in file handles"

class NoSuchPathError(Error):
    def __init__(self):
        self.msg = "Path does not exist!"