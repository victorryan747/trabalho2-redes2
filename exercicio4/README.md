# Exercício 4: Servidor de Hora com Threads (TCP)

Servidor TCP multithread que retorna a hora atual no formato `HH:MM:SS` e mantém um contador global de clientes atendidos sincronizado com `threading.Lock`.

## Dependências
Apenas bibliotecas nativas do Python 3.10+ (`socket`, `threading`, `argparse`, `datetime`).

## Como executar

1. Inicie o servidor:
```bash
python3 servidor.py --host 0.0.0.0 --porta 7000