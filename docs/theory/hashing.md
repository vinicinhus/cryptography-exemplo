# Funções Hash

As funções hash são algoritmos que transformam dados de qualquer tamanho em uma string de tamanho fixo, geralmente representada em formato hexadecimal. Elas são amplamente utilizadas para garantir a integridade dos dados.

## Propriedades das Funções Hash

1. **Determinística**: A mesma entrada sempre resultará na mesma saída.
2. **Rapidez de Computação**: A função deve ser rápida de computar para qualquer dado de entrada.
3. **Resistência à Colisão**: Deve ser difícil encontrar duas entradas diferentes que resultem no mesmo hash.
4. **Resistência à Pré-imagem**: Deve ser difícil reconstruir a entrada original a partir do hash.
5. **Difusão**: Uma pequena alteração na entrada deve produzir uma saída completamente diferente.

## Exemplos de Funções Hash

### MD5 (Message Digest Algorithm 5)

Embora amplamente usado no passado, o MD5 é considerado inseguro devido a vulnerabilidades que permitem colisões.

### SHA-1 (Secure Hash Algorithm 1)

SHA-1 é mais seguro que o MD5, mas ainda possui vulnerabilidades que foram exploradas com sucesso. Não é recomendado para novas aplicações.

### SHA-256 (Secure Hash Algorithm 256 bits)

Parte da família SHA-2, o SHA-256 é amplamente utilizado e considerado seguro. É usado em várias aplicações de segurança, incluindo certificados SSL e criptomoedas.

## Casos de Uso

- **Verificação de Integridade**: Verificação de arquivos e dados para garantir que não foram alterados.
- **Armazenamento de Senhas**: Armazenamento seguro de senhas em sistemas de autenticação.
- **Assinaturas Digitais**: Geração de hashes para assinaturas digitais, garantindo que os dados não foram alterados.
