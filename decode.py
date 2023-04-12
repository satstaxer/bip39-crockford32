from crockford32 import Crockford

crockford = Crockford()
with open("restored_encoded_wallet.txt", mode='r') as file:
  ip = file.read()
op = crockford.getBinary(ip)

opAll = ''.join(op)
excess = int(opAll[0:5], 2)
skip = 5 + 5 - excess
pinOpStr = opAll[skip:]
pinLen = int(pinOpStr[0:5], 2)

j = 1
if pinLen > 0:
  for i in range(pinLen):
    j = (i * 4) + 5
    print(int(pinOpStr[j:j+4],2), end='')
  print('')

opStr = pinOpStr[j+4:]
opLen = len(opStr)

for i in range(opLen // 11):
  j = i * 11
  print(crockford.wordsIndex(int(opStr[j:j+11],2)), end=' ')
print('')
