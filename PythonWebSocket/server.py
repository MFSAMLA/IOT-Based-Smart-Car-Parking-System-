import firebase_admin
from firebase_admin import credentials, db
import asyncio
import websockets
import json

# Initialize Firebase
cred = credentials.Certificate("smartparking.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://smart-car-parking-system-7af9d-default-rtdb.firebaseio.com"
})

# Create references
parkingDataF1 = db.reference('/data/floor1/sensorData')
parkingDataF2 = db.reference('/data/floor2/sensorData')

async def handle_client(websocket):
    print("Client connected")
   
    async for message in websocket:
        data = json.loads(message)
        
        if data['message'] == "update_parking":
            floor = data['floor']
            available = data['available']
            reserved = data['reserved']
            
            if floor == "1":
                parkingDataF1.update({
                    "availableSpots": available,
                    "reservedSpots": reserved
                })
            elif floor == "2":
                parkingDataF2.update({
                    "availableSpots": available,
                    "reservedSpots": reserved
                })
                
            await websocket.send("Parking data updated successfully")
            
        elif data['message'] == "get_parking":
            floor = data['floor']
            if floor == "1":
                data = parkingDataF1.get()
            elif floor == "2":
                data = parkingDataF2.get()
                
            await websocket.send(json.dumps(data))

def on_gate_change(event, floor):
    print(f"Gate change detected on {floor}: {event.event_type}")
    print(f"Data: {event.data}")

def listen_to_gate_changes():
    ref1 = db.reference('data/floor1/gates')
    ref2 = db.reference('data/floor2/gates')
    ref1.listen(lambda event: on_gate_change(event, 'Floor 1'))
    ref2.listen(lambda event: on_gate_change(event, 'Floor 2'))

async def start_server():
    listen_to_gate_changes()
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(start_server())