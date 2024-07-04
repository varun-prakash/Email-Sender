# Email Sender Script

This Python script sends a customized email with an attachment to multiple recipients. It uses the `smtplib` and `email` libraries to handle email sending.

## Features

- Send a custom email message to multiple recipients.
- Attach a file to each email.

## Prerequisites

- Python 3.x
- An email account (e.g., Gmail)

## Setup

1. **Clone the repository** (if applicable) or download the script file.
2. **Install required libraries**:

   ```bash
   pip install secure-smtplib
   ```

3. **Generate an App-Specific Password** (if using Gmail with 2-factor authentication):

   - Go to your [Google Account Security](https://myaccount.google.com/security).
   - Turn ON **2FAuthentication**.
   - Visit [Create app password](https://myaccount.google.com/apppasswords) to create app password.
   - Use the app password and it should work fine.

## Run the script

```bash
python email_sender.py
```
