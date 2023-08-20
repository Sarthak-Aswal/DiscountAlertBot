import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

def sendAlert(userMail,originalPrice,currentPrice,url):
    try:
        load_dotenv()
        message=f"Hello user,the price of your selected amazon product dropped from Rs{originalPrice} to Rs{currentPrice}.\n\nClick on the following link to buys it\n{url} "
        senderEmail = os.environ.get('mail')
        appPassword = os.environ.get('appPassword')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderEmail,appPassword)
        email=EmailMessage()
        email['From']=senderEmail
        email['To']=userMail
        email['Subject']='Discount Alert'
        email.set_content(message)
        server.send_message(email)
        server.quit()
        print("Email successfully sent")
        return
    except:
        print("Error in sending email")


