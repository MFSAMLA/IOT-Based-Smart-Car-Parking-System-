import asyncio
import websockets
import json
import random

async def send_data():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
        floor = input("Enter floor number (1/2): ")
        total_spots = 100 if floor == "1" else 150
        
        # Simulate random parking spot availability
        available = random.randint(0, total_spots)
        reserved = random.randint(0, 10)
        
        data = {
            "message": "update_parking",
            "floor": floor,
            "available": available,
            "reserved": reserved
        }
               
        await websocket.send(json.dumps(data))
        print(f"Data sent: {data}")

        response = await websocket.recv()
        print(f"Response: {response}")

asyncio.run(send_data())