# Loops through the actions and dispatches them.
from app.ableton_bridge import (
    set_tempo,
    create_midi_clip,
    add_drum_pattern,
    start_playback,
)


def execute_actions(action_response) -> None:
    for action in action_response.actions:
        if action.type == "set_tempo":
            set_tempo(action.bpm)

        elif action.type == "create_midi_clip":
            create_midi_clip(action.track, action.bars)

        elif action.type == "add_drum_pattern":
            add_drum_pattern(action.track, action.pattern)

        elif action.type == "start_playback":
            start_playback()

        else:
            print(f"[WARN] Unknown action type: {action.type}")