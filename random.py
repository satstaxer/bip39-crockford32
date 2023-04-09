import re
import sys

from crockford32 import Crockford
from collections import deque

crockford = Crockford()
ip=" "

binlist = deque()
ip = crockford.get_ip("Enter pin")
while re.search(r'[^0-9]', ip) is not None or len(ip) > 31:
  ip = crockford.get_ip("Enter pin (only numbers, no spaces, 31 or less digits)")

binlist.append(Crockford.binString(len(ip), 5))
for c in ip.strip()[0:32]:
  binlist.append(Crockford.binString(int(c), 4))

ip = crockford.get_ip("Enter words as binary string")
binlist.append(ip)
op = ''.join(binlist)
opLen = len(op)
excess = opLen % 5
binlist.appendleft("0" * (5-excess))
binlist.appendleft(Crockford.binString(excess, 5))

op = ''.join(binlist)
finalOp = crockford.getCrockford(op)
newFile = open("encoded_wallet.txt", "w")
newFile.write(finalOp)
newFile.close()
