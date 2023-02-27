from Crypto.Cipher import DES
from Crypto import Random
import sys

for arg in sys.argv[1:]:
    if arg == sys.argv[1]:
        iv = arg
    elif arg == sys.argv[2]:
        key = arg
    elif arg == sys.argv[3]:
        inputfile = arg
    elif arg == sys.argv[4]:
        outputfile = arg
    print(arg)


f = open(inputfile, encoding="utf-8")

text = ""
try:
    while True:
        text = f.read(1024)
        if not text:
            break
        plaintext = text
finally:
    f.close()
print(plaintext)

# cbc_key = Random.get_random_bytes(8)
cbc_key = bytes.fromhex(key)

print('=' * 100)
print('Key used: ', [x for x in cbc_key])

# iv = Random.get_random_bytes(8)
iv = bytes.fromhex(iv)


print("IV used: ", [x for x in iv])
print('=' * 100)

des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
des2 = DES.new(cbc_key, DES.MODE_CBC, iv)

print("Plaintext is: ", plaintext)

cipher_text = des1.encrypt(plaintext.encode("latin-1"))


print("Ciphertext is: ", cipher_text.decode("latin-1"))

with open(outputfile,"w",encoding='utf-8' ) as file:
    file.write(cipher_text.decode("latin-1"))

msg = des2.decrypt(cipher_text)
# print(msg)
print("Original Message", msg.decode("latin-1"))

print('=' * 100)