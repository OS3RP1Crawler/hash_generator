#!/usr/bin/python

BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE36_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"

# Courtesy of http://stackoverflow.com/questions/1119722/base-62-conversion-in-python
def baseN_encode(num, alphabet):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base         # num = num - (num / base)
        arr.append(alphabet[rem]) # O(N)
    arr.reverse()                 # O(N)
    return ''.join(arr)

def baseN_decode(string, alphabet):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

def base62_encode(num):
    return baseN_encode(num, BASE62_ALPHABET)

def base62_decode(num):
    return baseN_decode(num, BASE62_ALPHABET)

def base36_encode(num):
    return baseN_encode(num, BASE36_ALPHABET)

def base36_decode(num):
    return baseN_decode(num, BASE36_ALPHABET)
