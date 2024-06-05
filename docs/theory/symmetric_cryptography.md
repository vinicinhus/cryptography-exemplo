# Criptografia Simétrica

Na criptografia simétrica, a mesma chave é usada tanto para cifrar quanto para decifrar a informação. Esse método é rápido e eficiente para grandes volumes de dados, mas apresenta desafios na troca segura de chaves.

## Exemplos de Algoritmos Simétricos

### DES (Data Encryption Standard)

O DES é um algoritmo de criptografia de bloco que utiliza uma chave de 56 bits. Foi amplamente usado no passado, mas é considerado inseguro para uso moderno devido ao seu tamanho de chave relativamente pequeno.

### AES (Advanced Encryption Standard)

O AES é o padrão atual para criptografia simétrica. Ele suporta chaves de 128, 192 e 256 bits, oferecendo um alto nível de segurança. O AES é amplamente utilizado em várias aplicações, incluindo criptografia de dados em repouso e em transferência de dados.

## Vantagens e Desvantagens

### Vantagens

- **Rapidez**: Muito eficiente para grandes volumes de dados.
- **Simples de Implementar**: Relativamente simples em termos de implementação comparado a métodos assimétricos.

### Desvantagens

- **Distribuição de Chaves**: Requer um método seguro para troca de chaves.
- **Escalabilidade**: Menos escalável para grandes sistemas devido à necessidade de múltiplas chaves.

## Casos de Uso

A criptografia simétrica é ideal para cenários onde as partes envolvidas já compartilham uma chave secreta segura, como em redes privadas e sistemas de arquivos criptografados.
