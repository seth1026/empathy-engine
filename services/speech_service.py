import edge_tts
import asyncio

async def _generate_speech_async(text: str, rate: str, pitch: str, volume: str, filename: str):
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural",
        rate=rate,
        pitch=pitch,
        volume=volume
    )
    await communicate.save(filename)

def generate_speech(text: str, rate: str, pitch: str, volume: str, filename: str):
    """Synchronous wrapper for async edge-tts"""
    asyncio.run(_generate_speech_async(text, rate, pitch, volume, filename))