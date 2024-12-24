api = 'qHjafb2bkk8ORO9Vq17mT19AIb0JOX8SB75DutwW'

import cohere

def mensagemparaobot(promt):
    co = cohere.ClientV2(api_key=api)
    res = co.chat(
    model="command-r-plus-08-2024",
    messages=[
        {
            "role": "user",
            "content": promt,
        }
    ],)
    return res.message.content[0].text