import requests

def handler(request):
    body = request.get_json()
    webhook_url = body.get("webhook_url")
    message = body.get("message", "Hello from Web UI!")

    if not webhook_url:
        return {
            "statusCode": 400,
            "body": "Webhook URL is required"
        }

    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)

    return {
        "statusCode": response.status_code,
        "body": response.text
    }
