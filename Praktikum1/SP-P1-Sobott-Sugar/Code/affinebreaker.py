#! /usr/bin/python3
import argparse
import cracker
from aclib import decode, acDecrypt, acEncrypt

from logger import logger, logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using the affine cipher")
    parser.add_argument("path", help="File path")
    parser.add_argument("-v", action="store_true")
    args = parser.parse_args()
    

    if args.v:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    path = args.path
    
    with open(path, "r") as f:
        cipher_text = f.read()

        table = cracker.computeFrequencyTable(decode(cipher_text))
        most_frequent_chars = cracker.computeMostFrequentChars(table, 10)
        key_pairs = cracker.computeKeyPairs(most_frequent_chars)

        cracker.analyzeCipherText(cipher_text, key_pairs)



