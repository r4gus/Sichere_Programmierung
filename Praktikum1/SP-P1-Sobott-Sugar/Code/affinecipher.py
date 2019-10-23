#! /usr/bin/python3

import sys

from aclib import decode, acDecrypt, acEncrypt


def crypt(path, key, fun):
    """
    Encodes/ Decodes the file pointed to by 'path'
    using the specified function 'fun'.
    """
    k1, k2 = decode(key)

    with open(path, "r") as f:
        print(fun(k1, k2, f.read()))


if __name__ == "__main__":
    mode = sys.argv[1]
    key = sys.argv[2]
    path = sys.argv[3]
    
    if mode == "e":
        crypt(path, key, acEncrypt)
    elif mode == "d":
        crypt(path, key, acDecrypt)

