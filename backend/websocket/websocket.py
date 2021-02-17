import asyncio
import json
import random
import functools
import websockets


async def handler(websocket, path, queue):
    print("Established connection with client")
    while True:
        data = []
        while not queue.empty():
            data.append(queue.get())
        if data:
            print(data)
            await websocket.send(json.dumps(data))
        await asyncio.sleep(0.1)


def start_websocket(queue):
    start_server = websockets.serve(functools.partial(handler, queue=queue), "127.0.0.1", 8888)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
