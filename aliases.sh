
alias aes256="gpg --cipher-algo AES256 --batch --yes --passphrase-fd 0"
alias aes256_encrypt="read_password | aes256 --symmetric"
alias aes256_decrypt="read_password | aes256 -d"

function clear_unsafe_files {
  rm encoded_wallet.txt restored_encoded_wallet.txt 
}

function random_seed {
  bin="";for i in `seq 1 256`; do bin=$bin$(($RANDOM%2)) ;done
  echo "ibase=16;obase=2;"`echo $bin | shasum -a 256 -0 | cut -c1-2 | tr a-f A-F`""  | bc |xargs printf "$bin%08d"
}

function read_password {
  if [[ $ZSH == 0 ]]; then
    echo $(read -sp "Password: "; echo $REPLY)
  else
    echo $(read -s "?Password: ";echo $REPLY)
  fi
}

function wallet_encode_decode {
  python3 encode.py
  cp encoded_wallet.txt restored_encoded_wallet.txt 
  python3 decode.py
  rm restored_encoded_wallet.txt
}

function wallet_it {
  python3 encode.py
  echo "Encrypt encoded_wallet.txt"
  aes256_encrypt encoded_wallet.txt
  rm encoded_wallet.txt
  python3 encode_file.py
  rm encoded_wallet.txt.gpg
  python3 decode_file.py
  echo "\nDecrypt restored_encoded_wallet.txt.gpg"
  aes256_decrypt restored_encoded_wallet.txt.gpg > restored_encoded_wallet.txt
  python3 decode.py
  rm restored_encoded_wallet.txt
}

function restore_it {
  echo "cp $1 encoded_encrypted_wallet.txt"
  cp $1 encoded_encrypted_wallet.txt
  python3 decode_file.py
  rm encoded_encrypted_wallet.txt
  echo "\nDecrypt restored_encoded_wallet.txt.gpg"
  aes256_decrypt restored_encoded_wallet.txt.gpg > restored_encoded_wallet.txt
  python3 decode.py
  rm restored_encoded_wallet.txt
}
