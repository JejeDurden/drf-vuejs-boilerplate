from django.conf import settings
from mailjet_rest import Client


def send_mailjet_email(data):
    mailjet = Client(
        auth=(settings.EMAIL_API_KEY, settings.EMAIL_API_SECRET), version="v3.1"
    )
    mailjet.send.create(data=data)


def get_subject_prefix():
    if settings.ENV != "production":
        return f"[{settings.ENV}] "
    return ""
