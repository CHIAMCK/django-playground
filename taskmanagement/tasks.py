from django.core.mail import send_mail

from sec import celery_app


@celery_app.task(name='send_out_email')
def send_verification_email(subject, message, from_email, recipient_list, fail_silently):

    send_mail(
        'subject here',
        'here is the message',
        'fron@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
