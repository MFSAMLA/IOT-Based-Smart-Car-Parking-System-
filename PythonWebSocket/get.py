import asyncio
import websockets
import json

async def send_data():
    
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
       
        data = {
            "message" : "get_data"
            }
               
        # Send the data as JSON string
        await websocket.send(json.dumps(data))
        print("Data Request send successfully")
        
        # Receive the response
        response = await websocket.recv()
        print(f"DATA : {response}")

        # Receive the response
        response = await websocket.recv()
        print(f"Response from server: {response}")
       

# Start the client
asyncio.run(send_data())
