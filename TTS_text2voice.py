import asyncio
import edge_tts
from pydub import AudioSegment
from pydub.playback import play
import pydub
import io


async def tts(text, actor="zh-CN-XiaoyiNeural"):
    _voices = await edge_tts.VoicesManager.create()
    _voices = _voices.find(ShortName=actor)
    _communicate = edge_tts.Communicate(text, _voices[0]["Name"])
    _out = bytes()
    async for _chunk in _communicate.stream():
        if _chunk["type"] == "audio":
            _out += _chunk["data"]
    return _out


def get_text2voice(text_in):
    loop = asyncio.get_event_loop()

    raw_mp3 = loop.run_until_complete(tts(text_in))

    # raw_mp3 = asyncio.run(tts(text_in))
    mp3 = pydub.AudioSegment.from_file(io.BytesIO(raw_mp3))
    pydub.playback.play(mp3)
    # mp3_file = AudioSegment.from_file("speech.mp3", format="mp3")
    # play(mp3_file)