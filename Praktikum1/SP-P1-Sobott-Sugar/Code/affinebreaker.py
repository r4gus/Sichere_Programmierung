#! /usr/bin/python3
import argparse
import cracker
from aclib import decode, acDecrypt, acEncrypt

from logger import logger, logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=   "Break cipher texts encrypted " + 
                                                    "with the affine cipher algorithm")
    parser.add_argument("path", help="File path")
    parser.add_argument("-v", action="store_true", help="[v]erbose mode")
    parser.add_argument("--limit", action="store", type=int, default=10,
        help="Number of characters to try. 1 <= limit <= 26")
    args = parser.parse_args()
    

    if args.v:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    limit = args.limit
    path = args.path

    if not (0 < limit <= 26):
        print("error: limit must be an integer between 1 and 26.\n")
        parser.print_help()
        exit()
    
    try:
        with open(path, "r") as f:
            cipher_text = f.read()

            table = cracker.computeFrequencyTable(decode(cipher_text))
            most_frequent_chars = cracker.computeMostFrequentChars(table, limit)
            key_pairs = cracker.computeKeyPairs(most_frequent_chars)

            cracker.analyzeCipherText(cipher_text, key_pairs)
    except:
        print(  "error: The specified file could not be opened! Please ensure, that\n" + 
                "       you've provided the right path and that the file does exist.\n\n")
        parser.print_help()





