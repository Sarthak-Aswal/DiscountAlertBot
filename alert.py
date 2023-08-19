import os
from dotenv import load_dotenv
import smtplib

def sendAlert(userMail,originalPrice,currentPrice):
    load_dotenv()
    email = os.environ.get('mail')
    appPasssword = os.environ.get('appPassword')
    print(email,appPasssword)
