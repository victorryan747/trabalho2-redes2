---

### Exercício 2: Servidor Echo (UDP)[cite: 3]

#### `exercicio2/servidor.py`
```python
# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import socket
import argparse

# Tamanho maximo teorico de payload UDP em IPv4: 65535 - 20 (IP) - 8 (UDP) = 65507 bytes
MAX_UDP_PAYLOAD = 65507


def iniciar_servidor(host, porta):
    """Inicializa o servidor UDP de eco."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
        servidor.bind((host, porta))
        print(f"[SERVIDOR UDP] Ouvindo em {host}:{porta}...")

        try:
            while True:
                dados, endereco = servidor.recvfrom(MAX_UDP_PAYLOAD)
                mensagem = dados.decode("utf-8", errors="replace")
                ip, porta_cliente = endereco

                print(f"[RECEBIDO de {ip}:{porta_cliente}] {mensagem}")

                # Devolve a mesma mensagem para o remetente (eco)
                servidor.sendto(dados, endereco)

        except KeyboardInterrupt:
            print("\n[SERVIDOR UDP] Servidor encerrado.")
        except Exception as erro:
            print(f"[ERRO] Falha no servidor UDP: {erro}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor Echo UDP - Exercicio 2")
    parser.add_argument("--host", default="0.0.0.0", help="Endereco IP para bind (padrao: 0.0.0.0)")
    parser.add_argument("--porta", type=int, default=6000, help="Porta do servidor (padrao: 6000)")
    args = parser.parse_args()

    iniciar_servidor(args.host, args.porta)