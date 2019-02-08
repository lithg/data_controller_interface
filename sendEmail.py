import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = 'gclithg@gmail.com'
gmail_password = 'Izaxwq6206!'

msg = MIMEMultipart('alternative')
sent_from = gmail_user
to = ['gclithg@gmail.com']
subject = 'TITULO EMAIL MCC aaaaaaaa'

html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

part = MIMEText(html, 'html')
msg.attach(part)

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, msg.as_string())

try:    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...')
