import base64
from openai import OpenAI
from prompt import *
def chat_with_openai(system_prompt,user_input):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":system_prompt},
                  {"role": "user", "content":user_input}]
    )
    return response.choices[0].message

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def describe_image(image,system_prompt):
    client = OpenAI()
    image_path = image['path']
    user_prompt = image['caption']
    base64_image = encode_image(image_path)
    content = []
    if(user_prompt != ''):
        content = [
                    {
                        "type":"text",
                        "text": {
                            f'the image caption is {user_prompt}'
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ]
    else:
        content = [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":system_prompt},
            {
                "role": "user",
                "content": content,
            }
        ],
    )

    return response.choices[0].message
if __name__ == "__main__":
    image_path = '/home/ubuntu/PycharmProjects/combinRAG/src/tmp_data/OCR/ocr/images/071e44b72e537f126375a34a64ae966b1d47fca6ab30d2d4184cecb5eca0a118.jpg'

    pass