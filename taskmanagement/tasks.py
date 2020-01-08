from django.core.mail import send_mail

from sec import celery_app


# @celery_app.task(name='send_out_email')
# def send_verification_email():
#     send_mail(

#     )
