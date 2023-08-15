import openai
import gradio

openai.api_key = "<openai API keys>"

messages = [{"role": "system", "content": "Create a personal webpage for me, all in a single file. Ask me 3 questions first on whatever you need to know."}]

def AssistantChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=AssistantChatGPT, inputs = "text", outputs = "text", title = "My Assistant")

demo.launch(share=True)