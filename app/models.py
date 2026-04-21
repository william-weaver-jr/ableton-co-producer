# Defines your action schemas using Pydantic.
from typing import List, Literal, Union, Dict
from pydantic import BaseModel, Field


class SetTempoAction(BaseModel):
    type: Literal["set_tempo"]
    bpm: int = Field(..., ge=40, le=300)


class CreateMidiClipAction(BaseModel):
    type: Literal["create_midi_clip"]
    track: str
    bars: int = Field(..., ge=1, le=16)


class AddDrumPatternAction(BaseModel):
    type: Literal["add_drum_pattern"]
    track: str
    pattern: Dict[str, List[float]]


class StartPlaybackAction(BaseModel):
    type: Literal["start_playback"]


Action = Union[
    SetTempoAction,
    CreateMidiClipAction,
    AddDrumPatternAction,
    StartPlaybackAction
]

class ClaudeActionResponse(BaseModel):
    actions: List[Action]