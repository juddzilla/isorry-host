from openai import OpenAI
from .serializers import CompletionsSerializer
from datetime import datetime
from django.utils.timezone import make_aware

client = OpenAI()


def Request(messages):
    model = 'gpt-3.5-turbo'
    completion_request = client.chat.completions.create(
        model=model,
        messages=messages
    )    

    ai_created_at = make_aware(datetime.fromtimestamp(completion_request.created))
    data = {
        "ai_created_at": ai_created_at,
        "ai_id": completion_request.id,
        "completion_tokens": completion_request.usage.completion_tokens,        
        "message": completion_request.choices[0].message.content,
        "messages": messages,            
        "model": completion_request.model,
        "prompt_tokens": completion_request.usage.prompt_tokens,
    }

    serializer = CompletionsSerializer(data=data)    
    if serializer.is_valid():
        completion = serializer.save()
        return completion
    else:
        return None