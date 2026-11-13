---

### Exercício 10: Chat em Rede com WebSockets[cite: 5, 6]

Aqui incluí tanto o cliente em **HTML/JS** (`index.html`, muito prático para abrir várias abas no navegador) quanto o cliente em **Python** (`cliente.py`), cumprindo ambas as possibilidades previstas no documento[cite: 6].

#### `exercicio10/servidor.py`

# Trabalho 2 - Redes de Computadores 2
# Prof. Alessandro Vivas Andrade
# Integrantes: Víctor Ryan Vieira, Tayna Lino de Carvalho

import asyncio
import argparse
import websockets
from websockets.exceptions import ConnectionClosed

# Dicionario para armazenar {websocket: username}
clientes_conectados = {}


async def broadcast(mensagem, remetente=None):
    """Envia uma mensagem para todos os demais clientes conectados."""
    for ws in list(clientes_conectados.keys()):
        if ws != remetente:
            try:
                await ws.send(mensagem)
            except ConnectionClosed:
                clientes_conectados.pop(ws, None)


async def handler(websocket):
    """Gerencia a conexao WebSocket de cada cliente."""
    username = None
    try:
        # Primeira mensagem enviada pelo cliente define seu nome de usuario
        username = await websocket.recv()
        username = username.strip() or "Anonimo"
        clientes_conectados[websocket] = username

        print(f"[CONECTADO] Usuario '{username}' entrou no chat.")
        await broadcast(f"[SISTEMA] {username} entrou no chat.", websocket)

        async for mensagem in websocket:
            texto = mensagem.strip()
            if texto:
                print(f"[{username}]: {texto}")
                await broadcast(f"[{username}]: {texto}", websocket)

    except ConnectionClosed:
        print(f"[AVISO] Conexao encerrada inesperadamente por '{username or 'desconhecido'}'.")
    except Exception as erro:
        print(f"[ERRO] Erro no atendimento de '{username or 'desconhecido'}': {erro}")
    finally:
        if websocket in clientes_conectados:
            del clientes_conectados[websocket]
        if username:
            print(f"[DESCONECTADO] Usuario '{username}' saiu.")
            await broadcast(f"[SISTEMA] {username} saiu do chat.")


async def main(host, porta):
    """Inicia o servidor WebSocket assincrono."""
    print(f"[WEBSOCKET] Servidor escutando em ws://{host}:{porta}")
    async with websockets.serve(handler, host, porta):
        await asyncio.Future()  # Mantem o servidor rodando continuamente


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor de Chat WebSockets - Exercicio 10")
    parser.add_argument("--host", default="0.0.0.0", help="IP para bind (padrao: 0.0.0.0)")
    parser.add_argument("--porta", type=int, default=8765, help="Porta do servidor (padrao: 8765)")
    args = parser.parse_args()

    try:
        asyncio.run(main(args.host, args.porta))
    except KeyboardInterrupt:
        print("\n[WEBSOCKET] Servidor encerrado.")