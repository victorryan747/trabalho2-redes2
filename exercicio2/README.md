# Exercício 2: Servidor Echo (UDP)

Serviço de eco utilizando o protocolo UDP, com validação do tamanho máximo de datagrama (65.507 bytes) e tratamento de tempo limite (`timeout`).

## Dependências
Apenas bibliotecas padrão do Python 3.10+ (`socket`, `argparse`).

## Como executar

1. Inicie o servidor UDP:
```bash
python3 servidor.py --host 0.0.0.0 --porta 6000