from django.shortcuts import render, redirect

# Create your views here.
from sendmail.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
def HomeView(request):
    return redirect('contact')
def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'], 
                'message':form.cleaned_data['message'],
                }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'sender@gmail.com', ['receiver@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    form = ContactForm()
    return render(request, "email.html", {'form': form})
 
def successView(request):
    return HttpResponse('Success! Thank you for your message.')
