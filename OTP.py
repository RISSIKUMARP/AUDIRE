import smtplib
import random

def send_otp(to_email):
    # Generate a random OTP
    otp = str(random.randint(1000,9999))

    # Sender's email and password
    gmail_user = "201501010@rajalakshmi.edu.in"
    gmail_password = "REC202094420"

    # Email subject and body
    subject = 'OTP for your  account'
    body = 'Your OTP for verification is: ' + otp

    # Prepare the email
    email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (gmail_user, to_email, subject, body)

    try:
        # Send the email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, email_text)
        server.close()

        print('Email sent!')
    except Exception as e:
        print(e)
        print('Something went wrong...')

# Example usage
send_otp('201501034@rajalakshmi.edu.in')