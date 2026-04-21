# Ableton Co-producer

A fast MVP for controlling Ableton Live with prompts using Claude.

## Goal
Convert natural language prompts into structured music actions like:
- set tempo
- create MIDI clip
- add drum pattern
- start playback

## Current Status
This version uses a mocked Ableton bridge that prints actions to the console.

## Example Prompt
Create a dark trap drum loop at 140 BPM

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env