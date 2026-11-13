# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import socket
import threading
import argparse
import sys


def receber_mensagens(sock, ativo):
    """Thread dedicada para ouvir mensagens vindas do servidor continuamente."""
    while ativo.is_set():
        try:
            dados = sock.recv(1024)
            if not dados:
                print("\n[SISTEMA] Conexao encerrada pelo servidor.")
                ativo.clear()
                break
            print(dados.decode("utf-8"))
            print("> ", end="", flush=True)
        except OSError:
            break
        except Exception as erro:
            if ativo.is_set():
                print(f"\n[ERRO] Falha ao receber dados: {erro}")
            break


def iniciar_cliente(host, porta):
    """Conecta ao servidor de chat e gerencia o envio de mensagens."""
    nickname = ""
    while not nickname:
        nickname = input("Digite seu nome de usuario (nickname): ").strip()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((host, porta))
            # Envia o nickname assim que conecta
            cliente.sendall(nickname.encode("utf-8"))

            print(f"Conectado ao chat como '{nickname}'. Digite 'sair' para desconectar.")

            ativo = threading.Event()
            ativo.set()

            # Inicia a thread de leitura em paralelo
            thread_leitura = threading.Thread(
                target=receber_mensagens,
                args=(cliente, ativo),
                daemon=True
            )
            thread_leitura.start()

            while ativo.is_set():
                mensagem = input("> ").strip()
                if not ativo.is_set():
                    break

                if not mensagem:
                    continue

                if mensagem.lower() == "sair":
                    cliente.sendall("sair".encode("utf-8"))
                    ativo.clear()
                    print("Voce saiu do chat.")
                    break

                cliente.sendall(mensagem.encode("utf-8"))

    except ConnectionRefusedError:
        print(f"[ERRO] Nao foi possivel conectar ao servidor em {host}:{porta}.")
    except KeyboardInterrupt:
        print("\nSaindo do chat...")
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente de Chat TCP - Exercicio 3")
    parser.add_argument("--host", default="127.0.0.1", help="IP do servidor (padrao: 127.0.0.1)")
    parser.add_argument("--porta", type=int, default=5001, help="Porta do servidor (padrao: 5001)")
    args = parser.parse_args()

    iniciar_cliente(args.host, args.porta)