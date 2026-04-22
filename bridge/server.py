'''Optional local HTTP server if you want a middle layer between Claude and Ableton.'''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from pathlib import Path
import json

app = FastAPI()

COMMAND_FILE = Path("bridge/latest_commands.json")
COMMAND_FILE.parent.mkdir(parents=True, exist_ok=True)

class CommandEnvelope(BaseModel):
    command: str
    args: Dict[str, Any]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/command")
def command(envelope: CommandEnvelope):
    try:
        COMMAND_FILE.write_text(
            json.dumps(envelope.model_dump(), indent=2),
            encoding="utf-8"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "queued", "command": envelope.command}