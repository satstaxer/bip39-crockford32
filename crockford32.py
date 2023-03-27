
from functools import partial

class Crockford:
  wMap = {}
  cMap = {}
  chars, words = [], []
  charsLen, wordsLen = 0, 0
  def __init__(self):

    fp = open("crockford32.csv")
    Crockford.chars = list(map(partial(self.parseword, Crockford.cMap), enumerate(fp)))
    fp.close()

    fp = open('dict.txt')

    Crockford.words = list(map(partial(self.parseword, Crockford.wMap), enumerate(fp)))
    fp.close()

    Crockford.charsLen, Crockford.wordsLen = len(Crockford.chars), len(Crockford.words)

  def get_ip(self, stmt="Enter input"):
    print(stmt, ":", end=" ")
    ip = input()
    return ip.strip()

  def parseword(self, mapVar, ipLine):
    i, ip = ipLine
    cols = ip.strip().split(' ')
    for x in cols:
      mapVar[x] = i
    return cols[0]

  def lookup(self, mapVar, ip):
    if ip in mapVar:
      return mapVar[ip]
    else:
      return -1

  def index(self, arrVar, arrLen, i):
    if i < arrLen:
      return arrVar[i]
    else:
      return ""

  def crockfordLookup(self, ip):
    return self.lookup(Crockford.cMap, ip)

  def dictLookup(self, ip):
    return self.lookup(Crockford.wMap, ip)

  def crockfordIndex(self, i):
    return self.index(Crockford.chars, Crockford.charsLen, i)

  def wordsIndex(self, i):
    return self.index(Crockford.words, Crockford.wordsLen, i)

  def getCrockford(self, op):
    iLen = len(op) // 5
    base32word = []
    for i in range(iLen):
      j = i*5
      base32word.append(self.crockfordIndex(int(op[j:j+5], 2)))
      if i % 25 == 24:
        base32word.append("\n")

    return ''.join(base32word)

  def getNumbers(self, op):
    iLen = len(op) // 11
    print(iLen)
    numbers = []
    for i in range(iLen):
      j = i*11
      numbers.append(self.wordsIndex(int(op[j:j+11], 2))[0:4])

    print(' '.join(numbers))

  def getBinary(self, ip):
    op = []
    for c in ip:
      if c in self.cMap:
        op.append(Crockford.binString(self.crockfordLookup(c), 5))
    return op

  @classmethod
  def binString(cls, number, numBits):
    return bin(number)[2:].zfill(numBits)

