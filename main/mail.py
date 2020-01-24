from django.core.mail import send_mail

send_mail('Subject', 'Message', 'personal@example.com',
          ['duhhobo@gmail.com'], fail_silently=False,)
