from django.shortcuts import render
from .forms import NewsLetterForm
from .models import NewsLetterRecipients
from django.http import HttpResponseRedirect
from .email import send_welcome_email

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('home')
    else:
        form = NewsLetterForm()
    return render(request, 'index.html')
