from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method == 'POST':
        sub = request.POST.get('Subject')
        msg = request.POST.get('Message')
        email = request.POST.get('Email')
        print(sub,msg,email)
        
        send_mail(
            sub,msg,'xyz@gmail.com',
            [email]
        )
        return HttpResponse("Email Send")
    return render(request,'home.html')
