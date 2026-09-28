import asyncio
import os
from pathlib import Path

import edge_tts

TEXT = "Hello from EdgeTTS! This is a simple local hello world demo."
VOICE = "en-US-JennyNeural"
OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "hello.mp3"


async def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(str(OUTPUT_FILE))

    print(f"Saved audio to: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    asyncio.run(main())
