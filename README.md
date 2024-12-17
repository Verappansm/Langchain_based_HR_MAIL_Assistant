# HR Mail Assistant using LangChain

## Overview

This project is an automated **HR Mail Assistant** that uses the **LangChain framework** and **OpenAI's API** to streamline HR-related email tasks. The assistant:
1. Logs into a specified Gmail account.
2. Continuously checks for unread emails in the inbox.
3. Parses the email content and extracts details (e.g., leave requests).
4. Generates a structured email table using OpenAI's language model.
5. Stores the processed email data in a PostgreSQL database.
6. Sends the formatted table back to the HR email.

## Features

- **Automated Email Retrieval**: Checks for unread emails at regular intervals.
- **Content Parsing**: Extracts relevant information (like leave dates) from the email body.
- **Email Table Generation**: Uses OpenAI's API to create a structured HTML table summarizing email details.
- **Database Storage**: Saves processed email information into a PostgreSQL database.
- **Email Forwarding**: Sends the formatted email to the HR representative.

## Project Structure

```plaintext
hr_mail_assistant/
├── main.py              # Main script for checking and processing emails
├── database.py          # Database setup using SQLAlchemy
├── apikey.py            # OpenAI API key configuration
├── credentials.json     # Gmail OAuth credentials (to be configured)
├── token.json           # OAuth token for Gmail API
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation
```


## Prerequisites
1. Python 3.8+
2. PostgreSQL Database
3. Gmail Account with IMAP Access enabled
4. OpenAI API Key

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd hr-mail-assistant
