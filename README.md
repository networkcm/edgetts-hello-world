# edgetts-hello-world

A minimal EdgeTTS demo that speaks a short phrase and saves it as an MP3 file.

## Prerequisites

- Python 3.9+
- A working internet connection

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python hello.py
```

This will generate a file named `output/hello.mp3` with a sample voice message.

## Customize

Edit the `TEXT` and `VOICE` constants in `hello.py` to change the spoken output and the voice selection.
