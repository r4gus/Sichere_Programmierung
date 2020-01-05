#!/bin/python2

import sys

shellcode           = ""
shellcode_length    = 0

binary = open(sys.argv[1], 'rb')

for byte in binary.read():
    shellcode = shellcode + ("\\x" + byte.encode("hex"))
    shellcode_length += 1

print(shellcode)
print("\nLength: " + str(shellcode_length))
