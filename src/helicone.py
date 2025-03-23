from openai import OpenAI
import os

client = OpenAI(
  base_url="https://oai.helicone.ai/v1", # The request to OpenAI is routed from here
  default_headers={
    "Helicone-Auth": f"Bearer {os.getenv('CUSTOM_HELICONE_PUBLIC_KEY')}"
  }
)
chat_completion = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Can you tell me a joke"}]
)
# This is connected to Public Helicone deployment at https://us.helicone.ai/
print(chat_completion.choices[0].message.content)