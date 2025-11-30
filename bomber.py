import requests
import json

def send_sms(target_number, message):
    api_url = "https://api.bulksms.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic NjIwOTY2OTkwMTZGNEU4MzgwRDcxODk0QkU0ODg2MTItMDItQzoyMUZ6KjlDQjJwcmlwU1lZSzBkaDBQMDRCNDhvYQ=="
    }
    data = {
        "message": {
            "destination": target_number,
            "source": "Nighga",
            "content": message
        }
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    return response.json()

def main():
    target_number = input("Enter target phone number: ")
    message = input("Enter message: ")
    response = send_sms(target_number, message)
    print(response)

if __name__ == "__main__":
    main()