# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import socket
import argparse


def iniciar_cliente(host, porta):
    """Conecta ao servidor TCP e envia mensagens ate o usuario digitar 'sair'."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((host, porta))
            print(f"[CONECTADO] Conectado ao servidor {host}:{porta}")
            print("Digite suas mensagens abaixo (ou 'sair' para encerrar):")

            while True:
                mensagem = input("> ")

                # Verifica comando de saida
                if mensagem.strip().lower() == "sair":
                    print("Encerrando conexao com o servidor...")
                    break

                # Validacao para impedir envio de mensagens vazias
                if not mensagem.strip():
                    print("[AVISO] A mensagem nao pode ser vazia. Digite algum texto.")
                    continue

                cliente.sendall(mensagem.encode("utf-8"))
                resposta = cliente.recv(1024).decode("utf-8")
                print(f"[SERVIDOR]: {resposta}")

    except ConnectionRefusedError:
        print(f"[ERRO] Conexao recusada. Verifique se o servidor esta ativo em {host}:{porta}.")
    except KeyboardInterrupt:
        print("\n[CLIENTE] Operacao interrompida pelo usuario.")
    except Exception as erro:
        print(f"[ERRO] Falha na comunicacao: {erro}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente TCP - Exercicio 1")
    parser.add_argument("--host", default="127.0.0.1", help="IP do servidor (padrao: 127.0.0.1)")
    parser.add_argument("--porta", type=int, default=5000, help="Porta do servidor (padrao: 5000)")
    args = parser.parse_args()

    iniciar_cliente(args.host, args.porta)