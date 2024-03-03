import openai
import gradio

openai.api_key = "##"

messages = [{"role": "system", "content": "You are the smartest AI on earth"}]

def CustomChatGPT(Input):
    messages.append({"role": "user", "content": Input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "CORTEX")

demo.launch(share=True)
