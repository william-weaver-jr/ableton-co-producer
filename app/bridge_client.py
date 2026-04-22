'''Sends commands from Python to the local Ableton bridge.'''
import requests

BASE_URL = "http://127.0.0.1:8765"

def send_command(payload: dict) -> dict:
    response = requests.post(f"{BASE_URL}/command", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()