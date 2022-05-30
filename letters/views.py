from django.shortcuts import render
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            HttpResponseRedirect('news_today')
    else:
        form = NewsLetterForm()
    return render(request, 'index.html')
