from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


def encrypt_file(file_name, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_name, "rb") as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(file_name + ".enc", "wb") as f:
        f.write(cipher.iv)
        f.write(ciphertext)


def decrypt_file(file_name, key):
    with open(file_name, "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(file_name[:-4], "wb") as f:
        f.write(plaintext)


if __name__ == "__main__":
    # Geração de uma chave de 256 bits (32 bytes)
    key = os.urandom(32)
    file_name = r"src\encryption\aes\dados_sensiveis.txt"

    # Criptografar o arquivo
    encrypt_file(file_name, key)
    print(f"Arquivo {file_name} criptografado com sucesso!")

    # Descriptografar o arquivo
    decrypt_file(file_name + ".enc", key)
    print(f"Arquivo {file_name}.enc descriptografado com sucesso!")
