### Exercício 3: Chat em Rede (TCP)[cite: 4]

#### `exercicio3/servidor.py`
# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import socket
import threading
import argparse

# Dicionario compartilhado {socket_cliente: nickname} protegido por Lock
clientes = {}
lock_clientes = threading.Lock()


def broadcast(mensagem, remetente_conn=None):
    """Envia uma mensagem para todos os clientes conectados, exceto o remetente."""
    with lock_clientes:
        for conn in list(clientes.keys()):
            if conn != remetente_conn:
                try:
                    conn.sendall(mensagem.encode("utf-8"))
                except Exception:
                    # Remove cliente caso a conexao tenha caido
                    conn.close()
                    del clientes[conn]


def gerenciar_cliente(conn, endereco):
    """Gerencia o ciclo de vida de um participante do chat."""
    nickname = None
    try:
        # Primeiro pacote enviado pelo cliente deve ser o seu nickname
        dados_nick = conn.recv(1024).decode("utf-8").strip()
        if not dados_nick:
            conn.close()
            return

        nickname = dados_nick
        with lock_clientes:
            clientes[conn] = nickname

        print(f"[ENTROU] {nickname} ({endereco[0]}:{endereco[1]}) entrou no chat.")
        broadcast(f"\n[SISTEMA] {nickname} entrou na sala.", conn)

        while True:
            dados = conn.recv(1024)
            if not dados:
                break

            texto = dados.decode("utf-8").strip()
            if texto.lower() == "sair":
                break

            if texto:
                print(f"[{nickname}]: {texto}")
                broadcast(f"\n[{nickname}]: {texto}", conn)

    except Exception as erro:
        print(f"[ERRO] Conexao com {endereco} apresentou falha: {erro}")
    finally:
        # Remove o cliente da lista e avisa os demais participantes
        with lock_clientes:
            if conn in clientes:
                del clientes[conn]
        conn.close()

        if nickname:
            print(f"[SAIU] {nickname} saiu do chat.")
            broadcast(f"\n[SISTEMA] {nickname} saiu da sala.", None)


def iniciar_servidor(host, porta):
    """Inicia o servidor central do chat TCP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((host, porta))
        servidor.listen()

        print(f"[CHAT TCP] Servidor ativo em {host}:{porta}")

        try:
            while True:
                conn, endereco = servidor.accept()
                thread = threading.Thread(
                    target=gerenciar_cliente,
                    args=(conn, endereco),
                    daemon=True
                )
                thread.start()
        except KeyboardInterrupt:
            print("\n[CHAT TCP] Encerrando servidor...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor de Chat TCP - Exercicio 3")
    parser.add_argument("--host", default="0.0.0.0", help="IP para bind (padrao: 0.0.0.0)")
    parser.add_argument("--porta", type=int, default=5001, help="Porta do chat (padrao: 5001)")
    args = parser.parse_args()

    iniciar_servidor(args.host, args.porta)