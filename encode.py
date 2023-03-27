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

ip = crockford.get_ip("Enter number of words")
while ip != "" and re.search(r'[^0-9]', ip) is not None:
  ip = crockford.get_ip("Enter number of words (only numbers, no spaces)")

if ip == "":
  worLen = 0
else:
  wordLen = int(ip)
  i = 0
  ip = crockford.get_ip("Enter words seperated by space (i = %d)" %(i))

while ip != "":
  for word in ip.strip().split(" "):
    i = i+1
    while word not in crockford.wMap:
      word = crockford.get_ip("Replace word (%d) with valid dict entry" %(i))
    s = Crockford.binString(int(crockford.dictLookup(word)), 11)
    if i <= wordLen:
      binlist.append(s)
  if i >= wordLen:
    ip = ""
  else:
    ip = crockford.get_ip("Enter words seperated by space (i = %d)" %(i))

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
