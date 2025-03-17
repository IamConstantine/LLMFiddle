from portkey_ai import Portkey

client = Portkey(
    provider="anthropic",
    Authorization=""
)

# Example: Send a chat completion request
response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    model="claude-3-5-sonnet-20240620"
)
print(response.choices[0].message.content)