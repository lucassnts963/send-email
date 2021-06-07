import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config

host = 'smtp.gmail.com'
port = 587
user = config.USER
password = config.PASSWORD

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(user, password)


#Email Simples
message = 'Olá, mundo!'
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = 'lucassnts963@gmail.com'
email_msg['Subject'] = 'Assunto da mensagem'

email_msg.attach(MIMEText(message, 'plain'))


server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
#server.quit()


#Email com Html
message_html = '''
<html>
  <head></head>
  <body>
    <p>Olá!<br>
       {}<br>
       Aqui vai um <a href="http://www.python.org">link</a> sobre o python.
    </p>
  </body>
</html>
'''.format(email_msg['to'])
email_msg.attach(MIMEText(message_html, 'html'))

server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())


with open('./email.html', 'r') as f:
    html = f.read()
    
    email_msg.attach(MIMEText(html, 'html'))
    
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())


server.quit()