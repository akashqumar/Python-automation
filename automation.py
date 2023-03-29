import whisper
import requests
import subprocess
import os


def audio_converter():
    model = whisper.load_model('base')
    result = model.transcribe('command.mp3',fp16 = False)
    SpeechToText = result['text']
    print("audio_conver done")

    return SpeechToText


def request(SpeechToText):
    api_endpoint = "" //API ENDPOINT

    api_key = os.getenv("openai_api_key")

    request_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    request_data = {
        "model": "text-davinci-003",
        "prompt": f"Write python script to {SpeechToText}. Provide only code, no text",
        "max_tokens": 500,
        "temperature": 0.5
    }

    response = requests.post(api_endpoint, headers=request_headers, json=request_data)

    if response.status_code == 200:
        response_text = response.json()["choices"][0]["text"]
        with open("output2.py", "w") as file:
            file.write(response_text)
        print("request done")
    else:
        print(f"Request failed with status code: {str(response.status_code)}")
        
        return 0

def automate():

    python_path = "/Users/akash/miniforge3/bin/python"
    script_path = "/Users/akash/Documents/VS code/python-auto/output2.py"


    subprocess.run([python_path, script_path, "--arg1", "value1", "--arg2", "value2"])

    return 0

STT = audio_converter()
request(STT)
automate()
