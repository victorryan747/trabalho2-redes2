# Trabalho 2 - Redes de Computadores 2

**Instituição:** Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM)  
**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Data de Entrega:** 13/11/2026  

Integrantes do Grupo
Víctor Ryan Vieira, Tayna Lino de Carvalho

Objetivo Geral
Desenvolver habilidades práticas de programação em redes de computadores utilizando os protocolos TCP e UDP, além de manipulação de sockets, controle de concorrência com threads, análise de tráfego de rede e sistemas de chat em tempo real.

Requisitos Técnicos
- **Linguagem:** Python 3.10 ou superior.
- **Sistema Operacional de Desenvolvimento e Testes:** Linux.
- **Paretrização:** Uso de `argparse` para passagem de host e porta via linha de comando, evitando valores fixos no código.

 Estrutura do Repositório

O repositório está organizado em diretórios independentes para cada exercício prático:

* `exercicio1/`: Comunicação Cliente-Servidor TCP multithread (múltiplos clientes simultâneos).
* `exercicio2/`: Servidor e Cliente Echo UDP com validação de payload máximo (65.507 bytes) e timeout.
* `exercicio3/`: Sistema de Chat em Rede TCP com suporte a múltiplos usuários e broadcast[cite: 4].
* `exercicio4/`: Servidor de Hora TCP multithread com controle thread-safe de atendimentos (`threading.Lock`).
* `exercicio5/`: Análise de tráfego HTTP via Wireshark (métodos, URLs e códigos de status).
* `exercicio6/`: Análise do *Three-Way Handshake* e encerramento de conexões TCP via Telnet.
* `exercicio7/`: Resolução de nomes e análise de registros DNS.
* `exercicio8/`: Análise de tráfego ICMP (`ping`) e cálculo de RTT.
* `exercicio9/`: Análise do processo DORA no protocolo DHCP (`dhclient`).
* `exercicio10/`: Sistema de Chat em Tempo Real utilizando WebSockets (servidor em Python e clientes em Python e HTML/JS).

Como Executar

Cada diretório de exercício possui seu próprio arquivo `README.md` detalhando os comandos exatos de compilação, dependências necessárias e parâmetros de execução. 

Para dependências específicas (como a biblioteca `websockets` do Exercício 10), consulte o diretório correspondente.
