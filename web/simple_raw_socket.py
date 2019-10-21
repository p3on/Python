#!/usr/bin/env python3

import websocket, sys, asyncio
import websockets

if not (sys.argv[1]):
    print("Supply ip and port")
    exit()

outfile = open('socket_binary_data', 'w+b')

ws = websocket.WebSocket()
ws.connect("ws://" + sys.argv[1])

while True:
    try:
        binary_frame = ws.recv_frame()
        b = binary_frame.data
        print(b)
        outfile.write(b)

    except Exception as e:
        print("Error {}".format(e))
