# Trabalho 2 - Redes de Computadores 2

**Instituição:** Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM)  
**Disciplina:** Redes de Computadores 2  
**Professor:** Alessandro Vivas Andrade  
**Data de Entrega:** 13/11/2026  

---

## Integrantes do Grupo
* Víctor Ryan Vieira, Tayna Lino de Carvalho

---

## Objetivo Geral
Desenvolver habilidades práticas de programação em redes de computadores utilizando os protocolos TCP e UDP, além de manipulação de sockets, controle de concorrência com threads, análise de tráfego de rede e sistemas de chat em tempo real[cite: 1].

---

## Requisitos Técnicos
- **Linguagem:** Python 3.10 ou superior[cite: 2].
- **Sistema Operacional de Desenvolvimento e Testes:** Linux[cite: 2].
- **Paretrização:** Uso de `argparse` para passagem de host e porta via linha de comando, evitando valores fixos no código[cite: 2].

---

## Estrutura do Repositório

O repositório está organizado em diretórios independentes para cada exercício prático:

* `exercicio1/`: Comunicação Cliente-Servidor TCP multithread (múltiplos clientes simultâneos)[cite: 3].
* `exercicio2/`: Servidor e Cliente Echo UDP com validação de payload máximo (65.507 bytes) e timeout[cite: 3].
* `exercicio3/`: Sistema de Chat em Rede TCP com suporte a múltiplos usuários e broadcast[cite: 4].
* `exercicio4/`: Servidor de Hora TCP multithread com controle thread-safe de atendimentos (`threading.Lock`)[cite: 4].
* `exercicio5/`: Análise de tráfego HTTP via Wireshark (métodos, URLs e códigos de status)[cite: 5].
* `exercicio6/`: Análise do *Three-Way Handshake* e encerramento de conexões TCP via Telnet[cite: 5].
* `exercicio7/`: Resolução de nomes e análise de registros DNS[cite: 5].
* `exercicio8/`: Análise de tráfego ICMP (`ping`) e cálculo de RTT[cite: 5].
* `exercicio9/`: Análise do processo DORA no protocolo DHCP (`dhclient`)[cite: 5].
* `exercicio10/`: Sistema de Chat em Tempo Real utilizando WebSockets (servidor em Python e clientes em Python e HTML/JS)[cite: 5, 6].

---

## Como Executar

Cada diretório de exercício possui seu próprio arquivo `README.md` detalhando os comandos exatos de compilação, dependências necessárias e parâmetros de execução. 

Para dependências específicas (como a biblioteca `websockets` do Exercício 10), consulte o diretório correspondente[cite: 6].