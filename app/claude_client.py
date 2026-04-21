# Calls Claude and gets back structured actions.
from anthropic import Anthropic
from app.config import ANTHROPIC_API_KEY, MODEL_NAME

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def get_actions_from_claude(user_prompt: str, system_prompt: str) -> str:
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1200,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    parts = []
    for block in response.content:
        if getattr(block, "type", None) == "text":
            parts.append(block.text)

    return "".join(parts).strip()