'''Entry point. Runs the app, accepts user prompt, sends it through the pipeline.'''
import json
from pydantic import ValidationError

from app.claude_client import get_actions_from_claude
from app.prompt_handler import load_system_prompt
from app.models import ClaudeActionResponse
from app.action_executor import execute_actions


def main() -> None:
    print("Ableton AI MVP")
    print("Type a prompt like: Create a dark trap drum loop at 140 BPM")
    user_prompt = input("\nPrompt: ").strip()

    if not user_prompt:
        print("No prompt provided.")
        return

    system_prompt = load_system_prompt()

    raw_response = get_actions_from_claude(user_prompt, system_prompt)

    print("\n[Claude raw response]")
    print(raw_response)

    try:
        payload = json.loads(raw_response)
        # Support both Pydantic v2 (`model_validate`) and v1 (`parse_obj`).
        if hasattr(ClaudeActionResponse, "model_validate"):
            parsed = ClaudeActionResponse.model_validate(payload)
        else:
            parsed = ClaudeActionResponse.parse_obj(payload)
    except json.JSONDecodeError as exc:
        print(f"\n[ERROR] Invalid JSON from Claude: {exc}")
        return
    except ValidationError as exc:
        print(f"\n[ERROR] Response schema validation failed:\n{exc}")
        return

    print("\n[Executing actions]")
    execute_actions(parsed)


if __name__ == "__main__":
    main()