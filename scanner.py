import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import socket

def scan_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        return title
    except:
        return None

def detect_firewall(url):
    try:
        response = requests.get(url)
        headers = response.headers
        if 'Server' in headers:
            return headers['Server']
        else:
            return None
    except:
        return None

def detect_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except:
        return None

def detect_host_provider(url):
    try:
        ip_address = socket.gethostbyname(url)
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        return data['org']
    except:
        return None

def assess_ddos_vulnerability(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def main():
    root = tk.Tk()
    root.title("DDoS Assessment Tool")
    root.geometry("400x300")
    root.resizable(False, False)

    label = tk.Label(root, text="DDoS Assessment Tool")
    label.pack(pady=20)

    entry = tk.Entry(root, width=30)
    entry.pack(pady=20)

    button = tk.Button(root, text="Scan Website", command=lambda: scan(entry.get()))
    button.pack(pady=20)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=20)

    def scan(url):
        title = scan_website(url)
        firewall = detect_firewall(url)
        ip_address = detect_ip_address(url)
        host_provider = detect_host_provider(url)
        ddos_vulnerability = assess_ddos_vulnerability(url)

        if title:
            result_label.config(text=f"Title: {title}")
        else:
            result_label.config(text="Could not retrieve title.")

        if firewall:
            result_label.config(text=f"Firewall detected: {firewall}")
        else:
            result_label.config(text="No firewall detected.")

        if ip_address:
            result_label.config(text=f"IP Address: {ip_address}")
        else:
            result_label.config(text="Could not retrieve IP Address.")

        if host_provider:
            result_label.config(text=f"Host Provider: {host_provider}")
        else:
            result_label.config(text="Could not retrieve Host Provider.")

        if ddos_vulnerability:
            result_label.config(text="DDoS vulnerability detected.")
        else:
            result_label.config(text="No DDoS vulnerability detected.")

    root.mainloop()

if __name__ == "__main__":
    main()