from multiprocessing import Process
from .empatica.empatica_control_flow import empatica_main
from .eyetracker.eyetracker_control_flow import eyetracker_main
from .skeleton.skeleton_control_flow import skeleton_main

import asyncio
import json
import random
import websockets
from datetime import datetime


def start_processes():
    p1 = Process(target=empatica_main)
    p2 = Process(target=eyetracker_main)
    p3 = Process(target=skeleton_main)
    p1.start()
    p2.start()
    p3.start()

    start_websocket()


connected = set()
loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)


async def producer():
    """
    Get data from measurements
    Create JSON structure
    Add to queue
    :return: void
    """
    x = 100
    y = 100
    z = 5
    while True:
        x += random.randint(-1, 1)
        y += random.randint(-1, 1)
        z += random.randint(-5, 5)
        now = datetime.now()
        # time = now.strftime("%Y-%m-%d-T%H:%M:%S")
        time = now.strftime("%H:%M:%S")
        data = [
            {
                "name": "Stress",
                "number": x,
                "time": time
            },
            {
                "name": "Arousal",
                "number": y,
                "time": time
            },
            {
                "name": "Entertainment",
                "number": z,
                "time": time
            },
        ]
        if connected:
            print(connected)
            print("ADDED DATA TO QUEUE")
            await queue.put(data)
        await asyncio.sleep(1)


# TODO: Fix proper removal of closed clients
async def handler(websocket, path):
    """
    Automatically sends items from the queue to connected clients.
    :param websocket:
    :param path:
    :return: void
    """
    connected.add(websocket)
    try:
        print("Established connection with client")
        while True:
            data = await queue.get()
            print(data)
            await asyncio.wait([ws.send(json.dumps(data)) for ws in connected])
    finally:
        connected.remove(websocket)


def start_websocket():
    start_server = websockets.serve(handler, "127.0.0.1", 8888)
    loop.run_until_complete(asyncio.gather(
        start_server,
        producer(),
    ))
