import lief
import hashlib
import sys

def md5(data):
    return hashlib.md5(data).hexdigest()

bin = lief.parse(sys.argv[1])
key = 'FLAG: aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1DaV96YWQzOVVodyZsaXN0PVJEQ2lfemFkMzlVaHcmdD0xNXM='

with open(sys.argv[1], "rb") as f:
    content = bytearray(f.read())

section_text = bin.get_section(".encrypted")
for i in range(len(section_text.content)):
    content[section_text.offset + i] ^= ord(key[i % len(key)])

with open(sys.argv[1], "wb") as f:
    f.write(content)