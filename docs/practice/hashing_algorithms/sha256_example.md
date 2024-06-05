# Exemplo de Uso do SHA-256

SHA-256 é uma função hash criptográfica usada para garantir a integridade dos dados. Um caso de uso comum é verificar a integridade de arquivos baixados.

## Caso de Uso: Verificação de Integridade de Arquivos

Imagine que você baixou um arquivo de um site e quer verificar se o arquivo não foi corrompido durante o download.

### Exemplo em Python

```python
import hashlib

def hash_file(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Exemplo de uso
file_name = 'arquivo_baixado.zip'
hash_value = hash_file(file_name)
print("Hash SHA-256 do arquivo:", hash_value)

# Comparar com o hash fornecido pelo site
expected_hash = "valor_do_hash_fornecido_pelo_site"
if hash_value == expected_hash:
    print("O arquivo está íntegro.")
else:
    print("O arquivo foi corrompido.")
```

### Explicação

1. **Calcular o Hash:** O arquivo é lido em blocos e cada bloco é alimentado na função SHA-256 para calcular o hash do arquivo.

2. **Comparação de Hash:** O hash calculado é comparado com o hash fornecido pelo site para verificar a integridade do arquivo.

### Considerações de Segurança

- **Função Determinística:** SHA-256 sempre produzirá o mesmo hash para o mesmo arquivo.

- **Resistência a Colisões:** SHA-256 é projetado para ser resistente a colisões, tornando difícil encontrar dois arquivos diferentes com o mesmo hash.
