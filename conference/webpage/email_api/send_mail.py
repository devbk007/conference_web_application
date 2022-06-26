from .Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'webpage/email_api/client_secret.json' 
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def send(email, first_name, program, status):
    emailMsg = """Hi {user_name},
            
        Thanks for showing your interest towards {program}.
        
        Current Status : {status}.""".format(user_name=first_name, program = program, status = status)

    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = email
    mimeMessage['subject'] = 'Conference Registration Update'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)