# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import asyncio
import argparse
import websockets
from websockets.exceptions import ConnectionClosed


async def receber_mensagens(websocket):
    """Recebe mensagens do servidor de forma assincrona."""
    try:
        async for mensagem in websocket:
            print(f"\r{mensagem}\n> ", end="", flush=True)
    except ConnectionClosed:
        print("\n[SISTEMA] Conexao com o servidor foi encerrada.")


async def enviar_mensagens(websocket):
    """Le entradas do terminal sem bloquear o loop de eventos e envia ao servidor."""
    loop = asyncio.get_running_loop()
    while True:
        mensagem = await loop.run_in_executor(None, input, "> ")
        texto = mensagem.strip()

        if texto.lower() == "sair":
            await websocket.close()
            break

        if texto:
            await websocket.send(texto)


async def iniciar_cliente(host, porta):
    """Conecta ao servidor WebSocket e executa leitura e envio simultaneos."""
    uri = f"ws://{host}:{porta}"
    username = ""
    while not username:
        username = input("Digite seu nome de usuario: ").strip()

    try:
        async with websockets.connect(uri) as websocket:
            # Envia o nome de usuario ao conectar
            await websocket.send(username)
            print(f"Conectado em {uri} como '{username}'. Digite 'sair' para encerrar.")

            tarefa_receber = asyncio.create_task(receber_mensagens(websocket))
            tarefa_enviar = asyncio.create_task(enviar_mensagens(websocket))

            # Aguarda ate que uma das tarefas finalize (saida ou queda de conexao)
            _, pendentes = await asyncio.wait(
                [tarefa_receber, tarefa_enviar],
                return_when=asyncio.FIRST_COMPLETED
            )
            for tarefa in pendentes:
                tarefa.cancel()

    except ConnectionRefusedError:
        print(f"[ERRO] Servidor indisponivel em {uri}.")
    except Exception as erro:
        print(f"[ERRO] Falha na conexao WebSocket: {erro}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente de Chat WebSockets - Exercicio 10")
    parser.add_argument("--host", default="127.0.0.1", help="IP do servidor (padrao: 127.0.0.1)")
    parser.add_argument("--porta", type=int, default=8765, help="Porta do servidor (padrao: 8765)")
    args = parser.parse_args()

    try:
        asyncio.run(iniciar_cliente(args.host, args.porta))
    except KeyboardInterrupt:
        print("\nCliente encerrado.")