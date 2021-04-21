import asyncio
import functools
import json
import socket
import configparser

import pandas as pd
import websockets
from watchgod import awatch

from config import CONFIG_PATH


async def watcher(queue):
    async for changes in awatch('./crunch/output/'):
        for a in changes:
            file_path = a[1]
            # get last row of changed file
            df = pd.read_csv(file_path).iloc[-1]
            # format how we send it to frontend
            data = {"name": file_path[16:-4], "value": df.value, "time": df.time}
            print("reading from csv:", data)
            # put it queue so web socket can read
            await queue.put([data])


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

    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_PATH)
        use_localhost = config["websocket"].getboolean("use_localhost")
        port = int(config["websocket"]["port"])
    except FileNotFoundError:
        raise FileNotFoundError("Could not find config file")
    except KeyError:
        raise KeyError("Error reading config file at [websocket]")

    local_ip = socket.gethostbyname(socket.gethostname())
    ip = "127.0.0.1" if use_localhost else local_ip

    print("##################################################################")
    print("###### Paste the websocket ip on the frontend to connect")
    print("###### IP: ", ip)
    print("###### Port: ", port)
    print("##################################################################")

    start_server = websockets.serve(functools.partial(handler, queue=queue), ip, port)
    loop.run_until_complete(asyncio.gather(
        start_server,
        watcher(queue),
    ))
