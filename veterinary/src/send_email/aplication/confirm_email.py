# django
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils import timezone

# utils
from send_email.utils import token

# repositories
from send_email.repository import tkdr


def send_email(request, instance, rol) -> None:
    context = {
        'user':instance,
        'domain':get_current_site(request),
        'rol':rol,
        'id':urlsafe_base64_encode(force_bytes(instance.id)),
        'token':token.make_token(instance),
    }
    email_body = render_to_string(
        template_name='confirm_message.html',
        context=context
    )
    email = EmailMessage(
        subject='Confirmar correo electronico.',
        body=email_body,
        to=[instance.email]
    )
    email.content_subtype = 'html'
    email.send()
    tkdr.create(context['token'])