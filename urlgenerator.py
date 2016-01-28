#!/usr/bin/python

import base_conversion
import sys
from urlgenerator_errors import Error, InvalidArgument
from generator import Generator
from filewriter import FileWriter

def which_base(s):
    base = int(s)
    if base != 36 and base != 62:
        raise InvalidArgument("Not a valid base!")

    return base

def get_length(s):
    try:
        length = int(s)
        return length
    except ValueError:
        raise InvalidArgument("Not a valid length or amount!")

if __name__ == "__main__":
    if len(sys.argv) <= 5:
        print "Generates base36/base62 numbers."
        print "Usage: python urlgenerator <36/62> <length> <amount> <path> <no of files to generate?>"
        sys.exit(1)
    try:
        base = which_base(sys.argv[1])
        length = get_length(sys.argv[2])
        amount = get_length(sys.argv[3])
        path = sys.argv[4]
        files = 8
        if len(sys.argv) == 6:
            files = int(sys.argv[5])
    except Error as e:
        print e.msg
        sys.exit(1)

    encode = None
    decode = None

    if base == 62:
        encode = base_conversion.base62_encode
        decode = base_conversion.base62_decode
        alphabet = base_conversion.BASE62_ALPHABET
    else:
        encode = base_conversion.base36_encode
        decode = base_conversion.base36_decode
        alphabet = base_conversion.BASE36_ALPHABET

    generator = Generator(base, length, amount, encode, decode)

    try:
        with FileWriter(path, base, alphabet, files) as fileWriter:
            for i in generator:
                fileWriter.write(i)
    except Error as e:
        print e.msg
        sys.exit(1)
