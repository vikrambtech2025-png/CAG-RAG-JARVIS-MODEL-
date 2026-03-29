import requests

API_KEY = "sk_xkwamijx_zal0htahokZA7BRRcLDQeqDo"

def generate_response(prompt):
    url = "https://api.sarvam.ai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sarvam-m",  # adjust if needed
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    
    return response.json()["choices"][0]["message"]["content"]