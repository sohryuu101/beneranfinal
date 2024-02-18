from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import base64
import re
import time
import json
from dotenv import load_dotenv
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import set_key

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def gmail_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    load_dotenv()
    credentials = json.loads(os.getenv('GMAIL_API_CREDENTIALS'))
    token = json.loads(os.getenv('GMAIL_API_TOKEN'))
    
    if token:
        creds = Credentials.from_authorized_user_info(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                credentials, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        set_key('.env', 'GMAIL_API_TOKEN', creds.to_json())
        # with open('token.json', 'w') as token:
        #     token.write(creds.to_json())
    try:
        service = build('gmail', 'v1', credentials=creds)
        return service
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def create_message(sender, to, subject, message_text):
    """Create a message for an email.
    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg)

    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}

def send_message(service, user_id, message):
    """Send an email message.
    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.
    Returns:
    Sent Message.
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

if __name__ == "__main__":
    gmail_service()