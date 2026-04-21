# Temporary local stub for Ableton control. At first, this can just print actions.
# Later, this gets replaced with OSC, MIDI, Max for Live, or another bridge.
def set_tempo(bpm: int) -> None:
    print(f"[Ableton] Setting tempo to {bpm} BPM")


def create_midi_clip(track: str, bars: int) -> None:
    print(f"[Ableton] Creating {bars}-bar MIDI clip on track '{track}'")


def add_drum_pattern(track: str, pattern: dict) -> None:
    print(f"[Ableton] Adding drum pattern to '{track}'")
    for drum, notes in pattern.items():
        print(f"  - {drum}: {notes}")


def start_playback() -> None:
    print("[Ableton] Starting playback")