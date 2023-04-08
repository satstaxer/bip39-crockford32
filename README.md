# bip39-crockford32

BIP39 - https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki 

dict.txt is a copy of https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt

## Overview:
These steps are executed using alias `wallet_it` as defined in aliases.sh.
You can write down `encoded_encrypted_wallet.txt` to use it restore and retrieve you wallet.
1. `python3 encode.py`
    1. Ask for pin (upto 31 digits)
    1. Ask for number of words
    1. Ask for words
    1. Construct binary string
        1. Convert each digit of pin to 4 bit binary string
        1. Convert each word to corresponding index and subsequent 11 bit binary string
        1. Pad bits in the beginning so that binary string is divisible by 5
    1. Using a sliding window of 5 bits encode as Crockford-base32 character
    1. Write to file `encoded_wallet.txt`
2. `aes256_encrypt encoded_wallet.txt` - file `encoded_wallet.txt.gpg` will be created
3. `python3 encode_file.py` - write to `encoded_encrypted_wallet.txt` by reading bytes of `encoded_wallet.txt.gpg` and encode as Crockford-base32 character
4. `python3 decode_file.py` - write to `restored_encoded_wallet.txt.gpg` by decoding Crockford-base32 characters of `encoded_encrypted_wallet.txt` to binary
5. `aes256_decrypt restored_encoded_wallet.txt.gpg > restored_encoded_wallet.txt`
6. `python3 decode.py` - print pin and words to consosle
    
