import smtplib
import ssl


def news_digest(news):
    host = "smtp.gmail.com"
    port = 465
    username = "indulahari6@gmail.com"
    password = "qoeq lacl eays hetb"
    receiver = "vamshivam123456@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, news)