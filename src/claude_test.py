import anthropic as a
import os

os.environ['ANTHROPIC_API_KEY']=''

client = a.Anthropic()

model = {
    "sonnet" : "claude-3-7-sonnet-20250219",
    "haiku" : "claude-3-5-haiku-20241022",
}
message = client.messages.create(
    model=("%s" % model['haiku']),
    max_tokens=1000,
    temperature=1,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)
print(message.content)

