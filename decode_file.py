
from crockford32 import Crockford
crockford = Crockford()
op = []
with open("encoded_encrypted_wallet.txt", mode='r') as file:
  fileContents = file.read()
fileLength = len(fileContents)
binaryOp = crockford.getBinary(fileContents)
excess = 5 + 5 - int(binaryOp[0], 2)
bytesString = ''.join(binaryOp)[excess:]
bytesStringLen = len(bytesString)
newFile = open("restored_encoded_wallet.txt.gpg", "wb")
for i in range(bytesStringLen // 11):
  j = i * 11
  byte = int(bytesString[j:j+11],2)
  newFile.write(byte.to_bytes(1, byteorder='big'))

newFile.close()
