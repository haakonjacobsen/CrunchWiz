import asyncio
import json
import random

import websockets
from datetime import datetime


async def handler(websocket, path):
    print("Established connection with client")
    eye_baseline = 100
    wristband_baseline = 100
    montion_baseline = 5
    while True:
        eye_baseline = eye_baseline + random.randint(-1, 1)
        wristband_baseline = wristband_baseline + random.randint(-1, 1)
        montion_baseline = montion_baseline + random.randint(-5, 5)
        now = datetime.now()
        #time = now.strftime("%Y-%m-%d-T%H:%M:%S")
        time = now.strftime("%H:%M:%S")
        data = [
            {
                "name": "Eye tracker",
                "number": eye_baseline,
                "time": time
            },
            {
                "name": "Wristband",
                "number": wristband_baseline,
                "time": time
            },
            {
                "name": "Motion sensor",
                "number": montion_baseline,
                "time": time
            },
        ]
        await websocket.send(json.dumps(data))
        await asyncio.sleep(2)


start_server = websockets.serve(handler, "127.0.0.1", 8888)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
