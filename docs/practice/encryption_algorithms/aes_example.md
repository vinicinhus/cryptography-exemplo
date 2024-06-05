# Exemplo de Uso do AES

O AES (Advanced Encryption Standard) é amplamente utilizado para criptografar dados de maneira segura. Um caso de uso comum é a criptografia de dados em repouso, como arquivos em um disco.

## Caso de Uso: Criptografia de um Arquivo Sensível

Imagine que você tem um arquivo contendo informações sensíveis que precisa ser armazenado de forma segura. Vamos usar o AES para criptografar e descriptografar esse arquivo.

### Exemplo em Python

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(file_name, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_name, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(file_name + ".enc", 'wb') as f:
        f.write(cipher.iv)
        f.write(ciphertext)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(file_name[:-4], 'wb') as f:
        f.write(plaintext)

# Geração de uma chave de 256 bits (32 bytes)
key = os.urandom(32)
file_name = 'dados_sensiveis.txt'

# Criptografar o arquivo
encrypt_file(file_name, key)

# Descriptografar o arquivo
decrypt_file(file_name + '.enc', key)
```

### Explicação

1. **Geração da Chave:** A chave AES é gerada usando os.urandom(32) para obter uma chave de 256 bits.

2. **Criptografia:** O arquivo é lido em modo binário, padronizado para um múltiplo do tamanho do bloco do AES, e criptografado usando o modo CBC (Cipher Block Chaining). O IV (vetor de inicialização) é salvo junto com o texto cifrado.

3. **Descriptografia:** O arquivo cifrado é lido, o IV é extraído, e o texto é decifrado e desempadronizado.

### Considerações de Segurança

- **Gerenciamento de Chaves:** A chave de criptografia deve ser armazenada de maneira segura e não incluída no código fonte.

- **Uso do IV:** O IV deve ser único para cada criptografia, mas não precisa ser secreto.
