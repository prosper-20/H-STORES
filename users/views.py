from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib import auth

from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from sendgrid.helpers.mail import SandBoxMode, MailSettings
from django.conf import settings


User = get_user_model()

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Huff ,Username already exist')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Come On, Email was already Taken !')
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                mydict = {'username': username}
                user.save()
                messages.success(request, "Account creation successful!")
                html_template = 'users/register_email.html'
                html_message = render_to_string(html_template, context=mydict)
                subject = 'Welcome to Hertola Stores!'
                email_from = settings.DEFAULT_FROM_EMAIL
                recipient_list = [email]
                message = EmailMessage(subject, html_message,
                                       email_from, recipient_list)
                message.content_subtype = 'html'
                message.send()
                return redirect("/")
        else:
            messages.error(request, "Both passwords must match")
    else:
        return render(request, 'users/register.html')




def register2(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, "users/register2.html", context)




def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if "@" in username:
            present_user_username = User.objects.get(email=username).username
            user = auth.authenticate(username=present_user_username, password=password)
        else:
            user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"You are logged in as { user.username }")
            return redirect("/")
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect("login")
        
    else:
        return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
