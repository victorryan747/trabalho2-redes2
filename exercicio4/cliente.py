# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import socket
import argparse


def solicitar_hora(host, porta):
    """Conecta ao servidor, solicita a hora atual e exibe no console."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((host, porta))
            cliente.sendall(b"HORA")

            resposta = cliente.recv(1024).decode("utf-8")
            print(f"Hora atual recebida do servidor: {resposta}")

    except ConnectionRefusedError:
        print(f"[ERRO] Servidor indisponivel em {host}:{porta}.")
    except Exception as erro:
        print(f"[ERRO] Falha ao consultar hora: {erro}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente de Hora TCP - Exercicio 4")
    parser.add_argument("--host", default="127.0.0.1", help="IP do servidor (padrao: 127.0.0.1)")
    parser.add_argument("--porta", type=int, default=7000, help="Porta do servidor (padrao: 7000)")
    args = parser.parse_args()

    solicitar_hora(args.host, args.porta)