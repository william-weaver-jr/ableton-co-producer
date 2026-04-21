# Takes user input and prepares it for Claude.
from pathlib import Path

def load_system_prompt() -> str:
    prompt_path = Path("prompts/system_prompt.txt")
    return prompt_path.read_text(encoding="utf-8")