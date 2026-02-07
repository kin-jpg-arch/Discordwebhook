import os
import requests

def handler(request):
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    body = request.get_json()
    message = body.get("message", "Hello from Web UI!")

    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)

    return {
        "statusCode": response.status_code,
        "body": response.text
    }
