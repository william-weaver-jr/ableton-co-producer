# Loops through the actions and dispatches them.
from app.ableton_bridge import send_command


def execute_actions(action_response) -> None:
    for action in action_response.actions:
        payload = action.model_dump()
        command_type = payload.pop("type")

        result = send_command({
            "command": command_type,
            "payload": payload
        })

        print(f"[Bridge] {command_type} -> {result}")