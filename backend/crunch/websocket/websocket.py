import json
import websockets
import functools
import asyncio
import pandas as pd
from watchgod import awatch


async def watcher(queue):
    async for changes in awatch('./crunch/output/'):
        # get file path of changed file
        for a in changes:
            file_path = a[1]

        # get last row of changed file
        df = pd.read_csv(file_path).iloc[-1]
        # format how we send it to frontend
        data = {"name": file_path[16:-4], "value": df.value, "time": df.time}
        # put it queue so web socket can read
        await queue.put([data])


# TODO: Fix proper removal of closed clients
async def handler(websocket, path, queue):
    connected = set()
    connected.add(websocket)
    try:
        print("Established connection with client")
        while True:
            data = await queue.get()
            await asyncio.wait([ws.send(json.dumps(data)) for ws in connected])
    finally:
        print("CONNECTION WITH CLIENT LOST")


def start_websocket():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)

    start_server = websockets.serve(functools.partial(handler, queue=queue), "127.0.0.1", 8888)

    loop.run_until_complete(asyncio.gather(
        start_server,
        watcher(queue),
    ))
