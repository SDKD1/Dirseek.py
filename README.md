# PortSeeker.py

PortSeeker.py é uma ferramenta simples em Python para escanear portas abertas em hosts específicos ou em todos os hosts ativos na rede. A ferramenta estabelece uma conexão TCP via sockets para verificar a abertura das portas mais comuns em um endereço IP fornecido. Ideal para testes de penetração em redes e verificações de conectividade.

## Recursos
- **Escaneamento Rápido:** Verifica rapidamente uma ampla gama de portas comuns.
- **Personalização:** Permite modificar facilmente a lista de portas a serem verificadas.
- **Simplicidade:** Interface simples e fácil de usar, com entrada direta do IP.

## Uso
1. Execute o script.
2. Insira o endereço IP desejado quando solicitado.
3. Aguarde enquanto o script verifica as portas especificadas.

## Exemplo de Uso
```bash
$ python3 PortSeeker.py
Digite o IP: 192.168.0.1
Portas abertas em 192.168.0.1: 80, 443, 8080
