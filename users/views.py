from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from sendgrid.helpers.mail import SandBoxMode, MailSettings
from django.conf import settings
from django.views import View

# users/views.py
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, RedirectView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str # force_text on older versions of Django

from .forms2 import SignUpForm, token_generator, user_model
from .models import Profile



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




def login2(request):
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
            messages.info(request, f"You are logged in as { user.username }")
            return redirect("/")
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect("login")
        
    else:
        return render(request, 'users/new_login2.html') # You changed this to from new_login.html, login.html


def logout(request):
    auth.logout(request)
    return redirect("/")




# This part is for the django-sendgrid activation flow

class SignUpView(CreateView):
    form_class = SignUpForm 
    template_name = 'users/signup.html'
    success_url = reverse_lazy('check_email')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        
        user = form.save()
        user.is_active = False # Turns the user status to inactive
        user.save()

        form.send_activation_email(self.request, user)

        return to_return


class ActivateView(RedirectView):

    url = reverse_lazy('success')

    # Custom get method
    def get(self, request, uidb64, token):

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = user_model.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return super().get(request, uidb64, token)
        else:
            return render(request, 'users/activate_account_invalid.html')

class CheckEmailView(TemplateView):
    template_name = 'users/check_email.html'

class SuccessView(TemplateView):
    template_name = 'users/success.html'



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)



class MyPasswordResetView(View):
    def get(self, request, *args, **kwargs):
            return render(request, "users/forgot_password.html")
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        print(email)
        if User.objects.filter(email=email):
            messages.success(request, f"We've emailed you instructions for setting your password.If you don't receive an email, please make sure you've entered the address you registered with.")
            html_template = 'users/password_reset_email.html'
            html_message = render_to_string(html_template)
            subject = "Password Reset Link" 
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                email_from, recipient_list)
            message.content_subtype = "html"
            message.send()
            return render(request, "users/forgot_password.html")
        else:
            messages.error(request, "Sorry, didn't find a user with this email....")
            return render(request, "users/forgot_password.html")
