# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import socket
import argparse

MAX_UDP_PAYLOAD = 65507


def iniciar_cliente(host, porta, timeout):
    """Envia datagramas UDP ao servidor e aguarda o eco."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
        # Define tempo limite para aguardar resposta do servidor
        cliente.settimeout(timeout)

        print(f"[CLIENTE UDP] Configurado para enviar a {host}:{porta} (timeout: {timeout}s)")
        print("Digite mensagens para enviar (ou 'sair' para finalizar):")

        while True:
            try:
                texto = input("> ")

                if texto.strip().lower() == "sair":
                    print("Finalizando cliente UDP...")
                    break

                if not texto.strip():
                    print("[AVISO] Digite uma mensagem nao vazia.")
                    continue

                dados = texto.encode("utf-8")

                # Validacao do limite maximo de payload do protocolo UDP
                if len(dados) > MAX_UDP_PAYLOAD:
                    print(f"[ERRO] Mensagem excede o limite de {MAX_UDP_PAYLOAD} bytes ({len(dados)} bytes).")
                    continue

                cliente.sendto(dados, (host, porta))

                resposta, _ = cliente.recvfrom(MAX_UDP_PAYLOAD)
                print(f"[ECO DO SERVIDOR]: {resposta.decode('utf-8', errors='replace')}")

            except socket.timeout:
                print(f"[ERRO] Tempo limite de resposta ({timeout}s) esgotado. O servidor pode estar offline.")
            except KeyboardInterrupt:
                print("\n[CLIENTE UDP] Interrompido pelo usuario.")
                break
            except Exception as erro:
                print(f"[ERRO] Falha ao comunicar via UDP: {erro}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente Echo UDP - Exercicio 2")
    parser.add_argument("--host", default="127.0.0.1", help="IP do servidor (padrao: 127.0.0.1)")
    parser.add_argument("--porta", type=int, default=6000, help="Porta do servidor (padrao: 6000)")
    parser.add_argument("--timeout", type=float, default=5.0, help="Timeout em segundos (padrao: 5.0)")
    args = parser.parse_args()

    iniciar_cliente(args.host, args.porta, args.timeout)