from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


def homepage(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]} - {form.cleaned_data["subject"]}'
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = ['joshgarrants@gmail.com']
            try:
                send_mail(subject, message, sender,
                          recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent!')
    return render(request, 'main/home.html', {'form': form})
