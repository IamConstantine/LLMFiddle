from lunary import monitor
from openai import OpenAI

client = OpenAI()
# needs LUNARY_PUBLIC_KEY in env
monitor(client)

chat_completion = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
# This is connected to Public Lunary deployment at https://app.lunary.ai/
print(chat_completion.choices[0].message.content)
