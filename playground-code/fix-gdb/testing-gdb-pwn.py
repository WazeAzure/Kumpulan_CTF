from pwn import *

io = process('./a.out')

gdb.attach(io)

io.interactive()

