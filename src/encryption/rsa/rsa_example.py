from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# Geração de chaves RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()


def encrypt_password(password, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_password = cipher_rsa.encrypt(password.encode("utf-8"))
    return encrypted_password


def decrypt_password(encrypted_password, private_key):
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_password = cipher_rsa.decrypt(encrypted_password).decode("utf-8")
    return decrypted_password


if __name__ == "__main__":
    password = "SenhaTemp123"
    encrypted_password = encrypt_password(password, public_key)
    print("Senha Criptografada:", encrypted_password)

    decrypted_password = decrypt_password(encrypted_password, private_key)
    print("Senha Descriptografada:", decrypted_password)
