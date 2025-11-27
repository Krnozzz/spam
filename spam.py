#!/usr/bin/env python3

import smtplib
import getpass
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ANSI color codes
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[1;93m'
WHITE = '\033[1;97m'
CYAN = '\033[1;36;40m'

os.system("clear" if os.name != "nt" else "cls")

print(f"{WHITE}=== Email Sender ==={RESET}")
print(f"{YELLOW}For legitimate use only{RESET}\n")

# Email addresses
from_address = input(f"{YELLOW}From address: {WHITE}")
to_address = input(f"{YELLOW}To address: {WHITE}")

# SMTP Configuration
print(f"\n{YELLOW}Common SMTP servers:{RESET}")
print("Gmail: smtp.gmail.com (port 587)")
print("Outlook/Hotmail: smtp-mail.outlook.com (port 587)")
print("Yahoo: smtp.mail.yahoo.com (port 587)")
print("Custom: Enter your provider's SMTP server\n")

smtp_server = input(f"{YELLOW}SMTP server: {WHITE}")
smtp_port = input(f"{YELLOW}SMTP port (default 587): {WHITE}") or "587"

# Login credentials
username = input(f"{YELLOW}Your email: {WHITE}")
password = getpass.getpass(f"{YELLOW}Password/App Password: {WHITE}")

# Email content
subject = input(f"{YELLOW}Subject: {WHITE}")
message_body = input(f"{YELLOW}Message: {WHITE}")

# Create email message
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(message_body, 'plain'))

try:
    # Connect to server
    print(f"\n{CYAN}[*]{RESET} Connecting to server...")
    server = smtplib.SMTP(smtp_server, int(smtp_port))
    server.starttls()
    
    # Login
    print(f"{CYAN}[*]{RESET} Logging in...")
    server.login(username, password)
    
    # Send email
    print(f"{CYAN}[*]{RESET} Sending email...")
    server.send_message(msg)
    print(f"{GREEN}[✓]{RESET} Email sent successfully!")
    
    # Original spam section - fixed
    total = int(input(f"{YELLOW}Total spam: {WHITE}"))
    print(CYAN + "\n[*]" + WHITE + " Sending . . ." + WHITE)
    for i in range(total):
        server.send_message(msg)
        print(GREEN + "[~]" + WHITE + " mail sent")
    
    server.quit()
    
except smtplib.SMTPAuthenticationError:
    print(f"{RESET}[✗] Authentication failed. Check your credentials.")
    print("Note: Gmail/Outlook may require an app-specific password.")
except smtplib.SMTPException as e:
    print(f"{RESET}[✗] SMTP error: {e}")
except Exception as e:
    print(f"{RESET}[✗] Error: {e}")
