import requests
import os
import json

# request image generation from https://sd0.vm-app.cloud.cbh.kth.se/generate?prompt=PROMPT_HERE and download the file into ./img/id.png


def image(id, prompt):
    r = requests.get(
        f"https://sd0.vm-app.cloud.cbh.kth.se/generate?prompt={prompt}")

    # make sure the directory exists
    if not os.path.exists("./img"):
        os.makedirs("./img")

    with open(f"./img/{id}.png", 'wb') as f:
        f.write(r.content)

    # return filepath
    return f"{id}.png"


def text(prompt):
    body = json.dumps({"prompt": f"This is a conversation between user and llama, a friendly chatbot. respond in simple markdown. \n\n\nUser:{prompt}\n\n\nllama:",
                       "frequency_penalty": 0, "n_predict": 400, "presence_penalty": 0, "repeat_last_n": 256, "repeat_penalty": 1.18, "stop": ["</s>", "llama:", "User:"], "temperature": 1.5, "tfs_z": 1, "top_k": 40, "top_p": 0.5, "typical_p": 1})

    response = requests.post(
        "https://llama.app.cloud.cbh.kth.se/completion", data=body)
    res_json = response.json()
    content = res_json['content']

    return content
