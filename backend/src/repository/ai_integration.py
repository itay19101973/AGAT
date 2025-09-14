import http

import requests
from ..config import API_KEY
from ..schemes.ai_schemes import AiQuestion

url = "https://BGD15-PragatixAPI.agatdemo.com/firewallApi/v1/chat"


def send_question(data: AiQuestion):
    payload = {
        "APIKey": API_KEY,
        "Prompt": data.Prompt,
        "DataSource": data.DataSource

    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != http.HTTPStatus.OK:
        raise ValueError(f"API error {response.status_code}: {response.text}")
    data = response.json()
    return data["Response"]



