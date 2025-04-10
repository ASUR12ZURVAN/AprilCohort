import json
import asyncio
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer
import base64

ASSEMBLYAI_API_KEY = '946b88ba53ac4956a45526319da1dc2f'

class AssemblyAIConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("✅ WebSocket connection accepted")

        # Connect to AssemblyAI WebSocket with correct headers
        self.aai_ws = await websockets.connect(
            'wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000',
            additional_headers={
                "Authorization": ASSEMBLYAI_API_KEY
            }
        )
        print("✅ Connected to AssemblyAI")

        # Start background task to receive transcription
        self.receive_task = asyncio.create_task(self.receive_transcription())

    async def disconnect(self, close_code):
        await self.aai_ws.close()
        self.receive_task.cancel()
        print("❌ Disconnected")

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            # If you receive base64 audio directly as text
            await self.aai_ws.send(json.dumps({
                "audio_data": text_data
            }))
        elif bytes_data:
            # If you receive raw binary audio
            encoded_audio = base64.b64encode(bytes_data).decode("utf-8")
            await self.aai_ws.send(json.dumps({
                "audio_data": encoded_audio
            }))

    async def receive_transcription(self):
        try:
            async for message in self.aai_ws:
                result = json.loads(message)
                if result.get("message_type") == "FinalTranscript" and "text" in result:
                    await self.send(text_data=json.dumps({
                        "transcription": result["text"]
                    }))
        except websockets.exceptions.ConnectionClosed:
            print("❌ AssemblyAI WebSocket connection closed")
