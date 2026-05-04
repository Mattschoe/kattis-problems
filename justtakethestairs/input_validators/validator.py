import re
import sys
from sys import stdin

#SETUP
N_MIN = 1
N_MAX = 200_000
C_MIN = 1
C_MAX = 50
regex = r"^([1-9][0-9]*\s[1-9][0-9]*)$"

data = stdin.read()
if not data.endswith("\n"):
    print("1")
    exit(43)
lines = data.split('\n')
if lines[-1] != "":
    print("2")
    exit(43)
lines.pop()

# First line
if not re.fullmatch(regex, lines[0]):
    print("3")
    exit(43)
N, C = map(int, lines[0].split())
if not N_MIN <= N <= N_MAX:
    print("4")
    exit(43)
if not C_MIN <= C <= C_MAX:
    print("5")
    exit(43)

if len(lines) != 1 + N:
    print("6")
    sys.exit(43)

for i in range(1, 1+N):
    line = lines[i]
    if not re.fullmatch(regex, line):
        print("7")
        exit(43)
    S, F = map(int, line.split())
    if not 1 <= S <= C:
        print("8")
        exit(43)
    if not 1 <= F <= 5:
        print("9")
        exit(43)
if stdin.readline() != "":
    print("10")
    sys.exit(43)
exit(42)
