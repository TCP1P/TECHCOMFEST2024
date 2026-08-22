#!/usr/bin/env python3
import sys
import subprocess
import tempfile
import signal

TIMEOUT = 300
signal.alarm(TIMEOUT)

print("[ Input your lua code here (end with --END) ]", flush=True)

code = ""
while True:
    line = sys.stdin.readline()
    if line.startswith("--END"):
        break
    code += line
if len(code) > 1024:
    print("blud want to make a game 💀")
    exit(1)

with tempfile.NamedTemporaryFile(suffix=".lua") as f:
    f.write(code.encode())
    f.flush()
    try:
        subprocess.run(["/home/ctf/minivm/build/bin/minivm", f.name], timeout=TIMEOUT)
    except Exception as e:
        print(e, flush=True)
