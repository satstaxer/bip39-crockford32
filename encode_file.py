from crockford32 import Crockford

op = []
with open("encoded_wallet.txt.gpg", mode='rb') as file:
  fileContents = file.read()

fileLength = len(fileContents)
excess = (fileLength%5)
op.append(Crockford.binString(excess, 5))
op.append("0" * (5-excess))
for fileContent in fileContents:
  op.append(Crockford.binString(fileContent, 11))


crockford = Crockford()
with open("encoded_encrypted_wallet.txt", mode='w') as file:
  file.write(crockford.getCrockford(''.join(op)))
