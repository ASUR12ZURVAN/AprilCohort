import asyncio
import websockets

async def test_ws():
    uri = "wss://aprilcohort.onrender.com/ws/sentiment/"

    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Connected to WebSocket")
            await websocket.send("Hello from Python!")
            response = await websocket.recv()
            print("📩 Received:", response)
    except Exception as e:
        print("❌ Error:", e)

asyncio.run(test_ws())
