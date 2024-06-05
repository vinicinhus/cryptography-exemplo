# Troca de Chaves

A troca de chaves é um processo pelo qual duas partes estabelecem uma chave secreta compartilhada, que pode ser usada para comunicação segura subsequente. Este é um componente crítico em sistemas criptográficos.

## Métodos de Troca de Chaves

### Diffie-Hellman

O algoritmo Diffie-Hellman permite que duas partes gerem uma chave secreta compartilhada, mesmo que estejam se comunicando por um canal inseguro. Ele baseia-se na dificuldade de calcular logaritmos discretos.

#### Funcionamento Básico

1. **Escolha de Parâmetros Públicos**: Dois números primos grandes, `p` e `g`, são escolhidos.
2. **Cálculo de Valores**: Cada parte escolhe um valor secreto e calcula um valor público correspondente.
3. **Troca e Cálculo da Chave Compartilhada**: As partes trocam seus valores públicos e usam seus valores secretos para calcular a chave compartilhada.

### Elliptic Curve Diffie-Hellman (ECDH)

ECDH é uma variante do Diffie-Hellman que utiliza curvas elípticas. Ele oferece a mesma segurança com chaves menores, tornando-o mais eficiente.

## Vantagens e Desvantagens

### Vantagens

- **Segurança**: Permite a troca segura de chaves em canais inseguros.
- **Escalabilidade**: Pode ser usado em grandes sistemas distribuídos.

### Desvantagens

- **Complexidade**: Mais complexo em termos de implementação e configuração.
- **Desempenho**: Pode ser computacionalmente intensivo, especialmente para dispositivos com recursos limitados.

## Casos de Uso

- **Protocolos de Comunicação Segura**: Utilizado em protocolos como SSL/TLS para estabelecer uma sessão segura entre cliente e servidor.
- **Redes Privadas Virtuais (VPNs)**: Utilizado para estabelecer canais de comunicação seguros através da internet.
