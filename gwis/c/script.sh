#!/bin/bash
# compile to assembly for 32-bit architecture
gcc -S -m32 test.c -o test_asm.o
# compipe and assemble to executable for 32-bit architecture
gcc -c -m32 test.c -o test_exe
# use objdump to disassemble the executable
objdump -d -M intel test_exe > test_asm_bin.txt
# use xxd to make hexdump or binarydump of the executable
xxd test_exe > test_exe_hexdump.txt
xxd -b test_exe > test_exe_bindump.txt
