from openai import OpenAI
from completions.models import Completions
client = OpenAI()


def AI(messages):
    model = 'gpt-3.5-turbo'
    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    response = {
        "message": completion.choices[0].message.content,
        "token_usage": {
            "completion": completion.usage.completion_tokens,
            "prompt": completion.usage.prompt_tokens,
        },
        "model": model,
        "id": completion.id,
    }

    return completion