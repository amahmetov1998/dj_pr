from send_email.celery import app
from send_email.service import send


@app.task
def send_spam_email(user_email):
    send(user_email)
