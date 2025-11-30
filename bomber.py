import requests
import json
import random

def generate_otp(length=6):
    return ''.join(random.choices('0123456789', k=length))

def send_sms(target_number, message):
    api_url = "https://api.bulksms.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic NTkwM0VFODUyRDRCNDk3Q0FFQjFERURERjYwRTlGRjItMDItRjpRMFBFZkdjS1RySEFVTEdPRmJTZHZRdE5DQXlkTw=="
    }
    data = {
        "to": target_number[1:],  # Remove the leading 0
        "from": "Your Name",
        "body": message
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    if response.status_code == 403:
        print("Insufficient credits. Please purchase more credits to send SMS messages.")
    else:
        return response.json()

def main():
    target_number = input("Enter target phone number: ")
    otp = generate_otp()
    message = f"Your OTP is {otp}"
    response = send_sms(target_number, message)
    if response:
        print(response)

if __name__ == "__main__":
    main()