import openai

print("Welcome to ChatGPT Chat [Please type bellow your message]")
msg = input()

openai.api_key = "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"
completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [{"role": "user", "content": msg}]
)

print("ChatGPT: \n" + completion.choices[0].message.content)