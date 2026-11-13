# Exercício 3: Chat em Rede (TCP)

Sistema de chat multiusuário em tempo real sobre TCP utilizando threads no servidor (para gerenciar conexões e realizar *broadcast*) e no cliente (para envio e leitura simultâneos).

## Dependências
Apenas bibliotecas nativas do Python 3.10+ (`socket`, `threading`, `argparse`, `sys`).

## Como executar

1. Inicie o servidor do chat:
```bash
python3 servidor.py --host 0.0.0.0 --porta 5001