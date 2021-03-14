# import asyncio
# import json
# import random
#
# import websockets
# from datetime import datetime

# connected = set()


# async def producer():
#     x = 100
#     y = 100
#     z = 5
#     x += random.randint(-1, 1)
#     y += random.randint(-1, 1)
#     z += random.randint(-5, 5)
#     now = datetime.now()
#     time = now.strftime("%H:%M:%S")
#     data = [
#         {
#             "name": "Eye tracker",
#             "number": x,
#             "time": time
#         },
#         {
#             "name": "Wristband",
#             "number": y,
#             "time": time
#         },
#         {
#             "name": "Motion sensor",
#             "number": z,
#             "time": time
#         },
#     ]
#     await asyncio.sleep(2)
#     return data
#
#
# async def handler(websocket, path):
#     connected.add(websocket)
#     try:
#         print("Established connection with client")
#         while True:
#             data = await producer()
#             await asyncio.wait([ws.send(json.dumps(data)) for ws in connected])
#     finally:
#         connected.remove(websocket)
#
#
# start_server = websockets.serve(handler, "127.0.0.1", 8888)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
#
