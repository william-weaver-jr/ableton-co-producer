# Defines your action schemas using Pydantic.
from typing import List, Literal, Union
from pydantic import BaseModel, Field

class MidiNote(BaseModel):
    pitch: int = Field(..., ge=0, le=127)
    start: float = Field(..., ge=0)
    duration: float = Field(..., gt=0)
    velocity: int = Field(..., ge=1, le=127)

class SetTempoAction(BaseModel):
    type: Literal["set_tempo"]
    bpm: int = Field(..., ge=40, le=300)

class CreateMidiClipAction(BaseModel):
    type: Literal["create_midi_clip"]
    track: str
    slot: int = Field(..., ge=0)
    bars: int = Field(..., ge=1, le=16)

class AddMidiNotesAction(BaseModel):
    type: Literal["add_midi_notes"]
    track: str
    slot: int = Field(..., ge=0)
    notes: List[MidiNote]

class StartPlaybackAction(BaseModel):
    type: Literal["start_playback"]

class StopPlaybackAction(BaseModel):
    type: Literal["stop_playback"]

Action = Union[
    SetTempoAction,
    CreateMidiClipAction,
    AddMidiNotesAction,
    StartPlaybackAction,
    StopPlaybackAction
]

class ClaudeActionResponse(BaseModel):
    actions: List[Action]