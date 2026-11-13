# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import socket
import threading
import argparse
from datetime import datetime


def atender_cliente(conn, endereco):
    """Gerencia a comunicacao com um cliente especifico em uma thread separada."""
    ip, porta = endereco
    print(f"[NOVA CONEXAO] Cliente conectado: {ip}:{porta}")

    # Garante o fechamento seguro do socket do cliente ao sair do bloco
    with conn:
        while True:
            try:
                dados = conn.recv(1024)
                if not dados:
                    # Cliente encerrou a conexao
                    break

                mensagem = dados.decode("utf-8").strip()

                # Validacao de mensagem vazia no lado do servidor
                if not mensagem:
                    conn.sendall("Erro: mensagem vazia nao e permitida.".encode("utf-8"))
                    continue

                agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"[{agora}] [{ip}:{porta}] Mensagem: {mensagem}")

                resposta = f"Mensagem recebida pelo servidor as {agora}"
                conn.sendall(resposta.encode("utf-8"))

            except ConnectionResetError:
                print(f"[AVISO] Conexao encerrada abruptamente por {ip}:{porta}")
                break
            except Exception as erro:
                print(f"[ERRO] Falha no atendimento de {ip}:{porta}: {erro}")
                break

    print(f"[DESCONECTADO] Cliente {ip}:{porta} finalizou a sessao.")


def iniciar_servidor(host, porta):
    """Inicializa o socket TCP e aguarda conexoes de multiplos clientes."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        # Permite reutilizar a porta imediatamente apos fechar o servidor
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((host, porta))
        servidor.listen()

        print(f"[SERVIDOR TCP] Ativo em {host}:{porta}. Aguardando conexoes...")

        try:
            while True:
                conn, endereco = servidor.accept()
                # Cria uma thread para cada novo cliente conectado
                thread = threading.Thread(
                    target=atender_cliente,
                    args=(conn, endereco),
                    daemon=True
                )
                thread.start()
        except KeyboardInterrupt:
            print("\n[SERVIDOR TCP] Encerrando servidor...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor TCP Multithread - Exercicio 1")
    parser.add_argument("--host", default="0.0.0.0", help="Endereco IP para bind (padrao: 0.0.0.0)")
    parser.add_argument("--porta", type=int, default=5000, help="Porta do servidor (padrao: 5000)")
    args = parser.parse_args()

    iniciar_servidor(args.host, args.porta)