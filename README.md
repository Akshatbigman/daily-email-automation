# Daily Email Automation with Python

This Python project automates sending daily email reports, including attachments. The script is scheduled to send an email at a specific time every day. This project uses the `smtplib` library for sending emails and the `schedule` library for task scheduling.

## Features

- Sends daily emails with a custom HTML message.
- Attaches a file to the email (e.g., a report).
- Automates the process using the `schedule` library.

## Prerequisites

- Python 3.x
- Gmail account (or any other SMTP-supported email provider)
- `schedule` library

## Installation

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/Akshatbigman/daily-email-automation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd daily-email-automation
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the `daily_email.py` file.
2. Update the following values in the script with your own credentials:
   - `sender_email`: The email address from which you will send the email.
   - `receiver_email`: The recipient’s email address.
   - `password`: Your email account password (or app-specific password if using Gmail).
   - `filename`: Path to the file you want to attach (e.g., `report.pdf`).

3. Run the script:

    ```bash
    python daily_email.py
    ```

The email will be sent daily at the time specified in the script (default is 08:00 AM).
