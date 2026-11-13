### Exercício 4: Servidor de Hora com Threads (TCP)[cite: 4]

#### `exercicio4/servidor.py`
# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import socket
import threading
import argparse
from datetime import datetime

# Contador global de clientes atendidos e Lock para controle de concorrencia
contador_atendimentos = 0
lock_contador = threading.Lock()


def atender_solicitacao(conn, endereco):
    """Atende a solicitacao de hora de um cliente de forma thread-safe."""
    global contador_atendimentos
    ip, porta = endereco

    try:
        with conn:
            # Aguarda a requisicao do cliente
             _ = conn.recv(1024)

            agora = datetime.now()
            hora_formatada = agora.strftime("%H:%M:%S")
            timestamp_log = agora.strftime("%d/%m/%Y %H:%M:%S")

            # Secao critica protegida por Lock para atualizar o contador
            with lock_contador:
                contador_atendimentos += 1
                total_atual = contador_atendimentos

            conn.sendall(hora_formatada.encode("utf-8"))

            print(
                f"[{timestamp_log}] Solicitação atendida | "
                f"Cliente: {ip}:{porta} | "
                f"Hora enviada: {hora_formatada} | "
                f"Total de atendimentos: {total_atual}"
            )
    except Exception as erro:
        # Garante que falhas em um cliente nao interrompam o funcionamento do servidor
        agora_erro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{agora_erro}] [ERRO] Falha ao atender cliente {ip}:{porta}: {erro}")


def iniciar_servidor(host, porta):
    """Inicia o servidor de hora TCP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((host, porta))
        servidor.listen()

        print(f"[SERVIDOR DE HORA] Rodando em {host}:{porta}...")

        try:
            while True:
                conn, endereco = servidor.accept()
                thread = threading.Thread(
                    target=atender_solicitacao,
                    args=(conn, endereco),
                    daemon=True
                )
                thread.start()
        except KeyboardInterrupt:
            print("\n[SERVIDOR DE HORA] Servidor finalizado.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor de Hora Multithread - Exercicio 4")
    parser.add_argument("--host", default="0.0.0.0", help="IP para bind (padrao: 0.0.0.0)")
    parser.add_argument("--porta", type=int, default=7000, help="Porta do servidor (padrao: 7000)")
    args = parser.parse_args()

    iniciar_servidor(args.host, args.porta)