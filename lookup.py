import random
from crockford32 import Crockford

op = []

"""
if  ip:
  a = int(ip)
else:
  a = random.randrange(1, random_max)
return a
"""

def three_x(x):
    op.append(str(x%Crockford.wordsLen))
    new_x = None
    if x % 2 == 1:
        new_x = ((3*x) + 1)
    else:
        new_x = int(x / 2)

    if new_x == 1:
        return 1
    else:
        three_x(new_x)

op = []
crockford = Crockford()

a = "starting"
while a:
  a = crockford.get_ip("Enter word")
  if a:
    for i in a.split(' '):
      print(crockford.dictLookup(i), end=' ')
    print('')
print('numbers')
a = '1'
while a:
  a = crockford.get_ip("Enter number")
  if a:
    print(a)
    for i in map(int, a.split(' ')):
      print(crockford.wordsIndex(i), end=' ')
    print('')

"""
a = get_ip("Enter seed", 100)
x = get_ip("Enter randomizer", 100)

print(a, x, a*x)
three_x(a*x)
wallet = []
for i in range(12):
    word_idx = op[i] % word_len
    wallet.append(word_idx)

print(wallet)
"""
