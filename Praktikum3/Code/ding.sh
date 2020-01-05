#!/bin/sh

nasm -f elf64 $1 -o out.o
objcopy -O binary out.o out.bin
./convert.py out.bin
