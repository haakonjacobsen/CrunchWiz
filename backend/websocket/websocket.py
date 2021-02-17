import asyncio
import json
import random

import websockets


async def handler(websocket, path):
    print("Established connection with client")
    while True:
        data = [
            {
                "name": "Eye tracker",
                "number": random.randint(0, 1000)
            },
            {
                "name": "Wristband",
                "number": random.randint(0, 100)
            },
            {
                "name": "Motion sensor",
                "number": random.randint(-10, -5)
            },
        ]
        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)


start_server = websockets.serve(handler, "127.0.0.1", 8888)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
