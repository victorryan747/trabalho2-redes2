# Exercício 1: Cliente-Servidor (TCP)

Implementação de comunicação cliente-servidor utilizando sockets TCP em Python com suporte a múltiplos clientes simultâneos por meio de threads.

## Dependências
Não há dependências externas. Utiliza apenas bibliotecas nativas do Python 3.10+ (`socket`, `threading`, `argparse`, `datetime`).

## Como executar

1. Inicie o servidor em um terminal:
```bash
python3 servidor.py --host 0.0.0.0 --porta 5000