import openai

import base64
import os
import requests


def generate_image(details) -> str:
    OPENAI_TOKEN = "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"
    openai.api_key = OPENAI_TOKEN
    response = openai.Image.create(
        prompt=details,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url


def stable_diffuse():
    engine_id = "stable-diffusion-xl-1024-v1-0"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = "sk-6kKEKpEk656MeuFnnZXadikxdP4w7Y7TKrqoFNopBbumLx9L"
    if api_key is None:
        raise Exception("Missing Stability API key.")
    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": "A lighthouse on a cliff"
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))
    data = response.json()
    for i, image in enumerate(data["artifacts"]):
        with open(f"./out/v1_txt2img_{i}.png", "wb") as f:
            f.write(base64.b64decode(image["base64"]))
