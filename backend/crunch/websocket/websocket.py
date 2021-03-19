import asyncio
import functools
import json

import pandas as pd
import websockets
from watchgod import awatch


async def watcher(queue):
    async for changes in awatch('./crunch/output/'):
        file_paths = []
        # get file path of changed file
        for a in changes:
            file_path = a[1]
            # get last row of changed file
            df = pd.read_csv(file_path).iloc[-1]
            # format how we send it to frontend
            data = {"name": file_path[16:-4], "value": df.value, "time": df.time}
            print("reading from csv:", data)
            # put it queue so web socket can read
            await queue.put([data])


# TODO: Fix proper removal of closed clients
async def handler(websocket, path, queue):
    try:
        print("Established connection with client")
        while True:
            data = await queue.get()
            print("Sending:", data)
            await websocket.send(json.dumps(data))
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
