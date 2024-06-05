# Exemplo de Uso do bcrypt

bcrypt é uma função de hashing de senhas projetada para ser computacionalmente intensiva, tornando difícil para atacantes realizar ataques de força bruta. Um caso de uso comum é o armazenamento seguro de senhas.

## Caso de Uso: Armazenamento Seguro de Senhas

Imagine que você está desenvolvendo um sistema de autenticação e precisa armazenar senhas de maneira segura no banco de dados.

### Exemplo em Python

```python
import bcrypt

# Função para hashear a senha
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Função para verificar a senha
def check_password(hashed, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Exemplo de uso
password = "MinhaSenhaSegura123"
hashed_password = hash_password(password)
print("Senha Hasheada:", hashed_password)

# Verificação da senha
is_correct = check_password(hashed_password, password)
print("Senha Correta?", is_correct)
```

### Exemplo

1. **Hash da Senha:** A senha é hasheada usando `bcrypt.gensalt()` para gerar um salt único e `bcrypt.hashpw()` para hashear a senha com o salt.

2. **Verificação da Senha:** A senha fornecida pelo usuário é comparada com o hash armazenado usando `bcrypt.checkpw()`.

### Considerações de Segurança

- **Uso do salt:** bcrypt automaticamente gera um salt único para cada senha, aumentando a segurança.

- **Fator de Custo:** bcrypt permite ajustar o fator de custo, aumentando a dificuldade de ataques de força bruta.
