#!/usr/bin/python2

import sys

shellcode = ""
count   = 0

file = open(sys.argv[1], 'rb')

for byte in file.read():
    shellcode += "\\x" + byte.encode("hex")
    count += 1

print(shellcode)
print(count)
