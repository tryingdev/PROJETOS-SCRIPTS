import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def MandaEmail():
    try:
        emails = ['########','########']#destinatario
        fromaddr = "########"#email
        toaddr = ", ".join(emails)
        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "TESTE EMAIL AUTOMATIZADO"

        body = "\nTESTE EMAIL AUTOMATIZADO"

        msg.attach(MIMEText(body, 'plain'))

        filename = 'anderson_resultado.pdf'#anexos-path

        attachment = open('anderson_resultado.pdf', 'rb')#anexos

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.outlook.com', 587)
        server.starttls()
        server.login(fromaddr, "####")#senhaemail
        text = msg.as_string()
        server.sendmail(fromaddr, emails, text)
        server.quit()
        print('\nEmail enviado com sucesso!')

    except:
        print("\nErro ao enviar email")
