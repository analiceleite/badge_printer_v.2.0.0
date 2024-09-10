import os, random, threading
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_email(email, request):
    print("Entrou em send_email")
    try:
        random_token = random.randint(11111, 99999)
        request.session['randomToken'] = random_token
        recipient = []
        subject = "[RECUPERAÇÃO DE SENHA] - Badge Printer"
        sender = os.getenv("DEFAULT_FROM_EMAIL")
        recipient.append(email)
        html_message = render_to_string("email/token-request.html",{"subject": subject, "random_token": random_token})
        thread_send_email = threading.Thread(target=send_mail,
                                             args=(subject, html_message, sender, recipient))
        thread_send_email.start()
        print(random_token)
    except:
        pass