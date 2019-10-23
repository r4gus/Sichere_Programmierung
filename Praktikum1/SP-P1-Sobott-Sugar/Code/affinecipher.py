#! /usr/bin/python3

import sys
import argparse

from aclib import decode, acDecrypt, acEncrypt


def crypt(path: str, key: str, fun) -> None:
    """
    Encodes/ Decodes the file pointed to by 'path'
    using the specified function 'fun'.
    """
    k1, k2 = decode(key)

    with open(path, "r") as f:
        print(fun(k1, k2, f.read()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using the affine cipher")
    parser.add_argument("mode", choices=["e", "d"], help="[e]ncrypt or [d]ecrpyt the file")
    parser.add_argument("key", help="String with exactly two lower case ascii letters")
    parser.add_argument("path", help="File path")
    args = parser.parse_args()

    mode = args.mode
    key = args.key
    path = args.path
    
    if mode == "e":
        crypt(path, key, acEncrypt)
    elif mode == "d":
        crypt(path, key, acDecrypt)

