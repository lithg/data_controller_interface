#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dados


me = "your@email.com"
you = "your@email.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "MCC - PENINTENCIA"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
        <html lang="en">
        <body>

        <div class="container">
            <table border='1',cellpadding='10',cellspacing ='0', width ='900'>
            <tr>
            <td bgcolor = '#bed3f4', Align = 'center', width = '125'>OPERAÇ.</td>
            <td bgcolor = '#bed3f4', Align = 'center', width = '125'>DATA</td>
            <td bgcolor = '#bed3f4', Align = 'center', width = '136'>HORA</td>
            <td bgcolor = '#F6F14E', Align = 'center', width = '250'>PRESSÃO</td>
            <td bgcolor = '#8EF64E', Align = 'center', width = '250'>UMIDADE</td>
            <td bgcolor = '#F6B44E', Align = 'center', width = '240'>TEMPERATURA</td>
            </tr>
            </table>


            <table border='1',cellpadding='10',cellspacing ='0', width = '900'>
            <tr>
            <td bgcolor = '#bed3f4', Align = 'center', width = '85'></td>
            <td bgcolor = '#bed3f4', Align = 'center', width = '85'></td>
            <td bgcolor = '#bed3f4', Align = 'center', width = '85'></td>
            <td bgcolor = '#F3FF33', Align = 'center', width = '50'>MIN</td>
            <td bgcolor = '#F3FF33', Align = 'center', width = '50'>MAX</td>
            <td bgcolor = '#F3FF33', Align = 'center', width = '50'>MED</td>
            <td bgcolor = '#07F22E', Align = 'center', width = '50'>MIN</td>
            <td bgcolor = '#07F22E', Align = 'center', width = '50'>MÁX</td>
            <td bgcolor = '#07F22E', Align = 'center', width = '50'>MED</td>
            <td bgcolor = '#F28D27', Align = 'center', width = '50'>MIN</td>
            <td bgcolor = '#F28D27', Align = 'center', width = '50'>MÁX</td>
            <td bgcolor = '#F28D27', Align = 'center', width = '50'>MED</td>
            </tr>
            </table>

            <table border='1',cellpadding='10',cellspacing ='0', width = '900'>
            <tr>
            <td bgcolor = '#bed3f4', Align = 'center', width = '85', height = '100'>RELATÓRIO</td>
            <td bgcolor = '#bed3f4', Align = 'center', width = '85', height = '100'>""" + dados.datas[0] + """</td>
            <td bgcolor = '#bed3f4', Align = 'center', width = '85', height = '100'>""" + dados.horas[0] + """</td>

            <td bgcolor = '#F3FF33', Align = 'center', width = '50'>""" + dados.min1 + """</td>
            <td bgcolor = '#F3FF33', Align = 'center', width = '50'>""" + dados.max1 + """</td>
            <td bgcolor = '#F3FF33', Align = 'center', width = '50'>""" + dados.med1 + """</td>
            <td bgcolor = '#07F22E', Align = 'center', width = '50'>""" """</td>
            <td bgcolor = '#07F22E', Align = 'center', width = '50'>"""  """</td>
            <td bgcolor = '#07F22E', Align = 'center', width = '50'>""" """</td>
            <td bgcolor = '#F28D27', Align = 'center', width = '50'>"""  """</td>
            <td bgcolor = '#F28D27', Align = 'center', width = '50'>"""  """</td>
            <td bgcolor = '#F28D27', Align = 'center', width = '50'>""" """</td>
            </tr>
            </table>

        </body>
        </html>
        """

# Record the MIME types of both parts - text/plain and text/html.
# part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
# msg.attach(part1)
msg.attach(part2)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('your@email.com', 'password')
    server.sendmail(me, you, msg.as_string())
    server.close()
    print('Email enviado!')

except:

    print('Falha no envio...')

