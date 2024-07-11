import smtplib
import ssl


def news_digest(news):
    host = "smtp.gmail.com"
    port = 465
    username = "user_email"
    password = "your_apppassword"
    receiver = "receiver_email"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, news)
