from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER


def send(user_email):
    send_mail(
        subject='',
        message='',
        from_email=EMAIL_HOST_USER,
        recipient_list=[user_email],
    )
