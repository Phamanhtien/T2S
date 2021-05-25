# coding=utf8
import time
import requests
from requests.structures import CaseInsensitiveDict


def request_api(content):
    url = "https://api.zalo.ai/v1/tts/synthesize"

    headers = CaseInsensitiveDict()
    headers["apikey"] = "yCxg51bJN6OnxhnY1tbIqYBG99aDiKiX"
    headers["Content-Type"] = "text/plain; charset=utf-8"

    content = content

    data = {
        "input":content,
        "speaker_id":"1"
    }
    data["input"] = str(data["input"]).encode('utf-8')
    data["speaker_id"] = str(data["speaker_id"]).encode('utf-8')

    resp = requests.post(url, headers=headers, data=data)
    time.sleep(3)
    return(resp.json())

