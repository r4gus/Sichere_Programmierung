#! /usr/bin/python3

import sys
import argparse
from string import ascii_lowercase

from aclib import decode, acDecrypt, acEncrypt


def crypt(path: str, key: str, fun) -> None:
    """
    Encodes/ Decodes the file pointed to by 'path'
    using the specified function 'fun'.
    """
    k1, k2 = decode(key)
    
    try:
        with open(path, "r") as f:
            print(fun(k1, k2, f.read()))
    except FileNotFoundError:
        print(  "usage: affinecipher.py [-h] {e,d} key path\n" +
                "error: The specified file could not be opened! Please ensure, that\n" + 
                "       you've provided the right path and that the file does exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using the affine cipher")
    parser.add_argument("mode", choices=["e", "d"], help="[e]ncrypt or [d]ecrpyt the file")
    parser.add_argument("key", help="String with exactly two lower case ascii letters")
    parser.add_argument("path", help="File path")
    args = parser.parse_args()

    mode = args.mode
    key = args.key
    path = args.path

    if len(key) != 2 or not key[0] in ascii_lowercase or not key[1] in ascii_lowercase:
        print(  "usage: " + sys.argv[0] +  "[-h] {e,d} key path\n" +
                "error: Invalid key pair. Use '-h' for help.")
    else:
        if mode == "e":
            crypt(path, key, acEncrypt)
        elif mode == "d":
            crypt(path, key, acDecrypt)

