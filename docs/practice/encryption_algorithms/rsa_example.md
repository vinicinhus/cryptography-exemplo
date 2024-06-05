# Exemplo de Uso do RSA

O RSA é frequentemente utilizado para criptografia de mensagens curtas, troca de chaves e assinaturas digitais. Um caso de uso comum é o envio seguro de uma senha temporária.

## Caso de Uso: Envio Seguro de Senha Temporária

Imagine que você precisa enviar uma senha temporária de maneira segura para um usuário. Você pode usar o RSA para criptografar a senha antes de enviá-la.

### Exemplo em Python

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Geração de chaves RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Função para criptografar a senha
def encrypt_password(password, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_password = cipher_rsa.encrypt(password.encode('utf-8'))
    return encrypted_password

# Função para descriptografar a senha
def decrypt_password(encrypted_password, private_key):
    private_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_password = cipher_rsa.decrypt(encrypted_password).decode('utf-8')
    return decrypted_password

# Exemplo de uso
password = "SenhaTemp123"
encrypted_password = encrypt_password(password, public_key)
print("Senha Criptografada:", encrypted_password)

decrypted_password = decrypt_password(encrypted_password, private_key)
print("Senha Descriptografada:", decrypted_password)
```

### Explicação

1. **Geração de Chaves:** As chaves RSA (pública e privada) são geradas usando um tamanho de 2048 bits.

2. **Criptografia:** A senha é criptografada usando a chave pública e o algoritmo `PKCS1_OAEP`.

3. **Descriptografia:** A senha criptografada é decifrada usando a chave privada.

### Considerações de Segurança

- **Tamanho da Chave:** Chaves maiores oferecem mais segurança, mas são mais lentas.

- **Proteção da Chave Privada:** A chave privada deve ser mantida segura e nunca compartilhada.
