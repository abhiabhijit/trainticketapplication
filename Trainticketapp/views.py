from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
import random
from .forms import SignupForm,LoginForm,PasswordForm,changepass
from django.contrib.auth.models import User
from django.core.mail import send_mail
# from email.header    import Header
# from email.mime.text import MIMEText
# from getpass         import getpass
# from smtplib         import SMTP_SSL
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail

#sign up page
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.phoneno = form.cleaned_data.get('phoneno')
            print(user.phoneno)
            user.save()
            to_email = form.cleaned_data.get('email')

            try:
                send_mail(
                    'Email Confirmation',
                    render_to_string('auth/account_activation_email.html', {
                 'user': user,
                 'uid': user.pk,

             }),
                    'abhijitastlar@gmail.com',
                    [to_email],
                )
            except:

                user.delete()
                return HttpResponse('Invalid email id . Doesnt exists')



            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})
#login page code
def login_page(request):
    form=LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user = authenticate(request,username=username, password=password)

        print(user)
        if user is not None:
            login(request,user)
            #print(request.user.is_authenticated())
            #context['form'] = LoginForm()

            return redirect("home")
        else:
            messages.success(request, ('Provide valid password'))
            print("Error")


    return  render(request,"auth/login.html",context)


@login_required
def changepassword(request):
    u = request.user
    if request.method == 'POST':
        form = changepass(request.POST or None)
        if form.is_valid():
            print(u)

            password=form.cleaned_data.get('password')
            print(password)
            u.set_password(password)
            u.save()

        return HttpResponse('Password changed')
    else:
        form = changepass()
    return render(request, 'auth/password_recovery.html', {'form': form})


#email confirmation
def activate(request,uidb64):

    try:
        uid = uidb64
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None  :
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        print(user)
        return redirect('home')
    else:
        return render(request, 'auth/account_activation_invalid.html')


def index(request):
    return render(request,'home.html',{})


@login_required
def logout(request):
    django_logout(request)
    return  redirect('home')



#logout request
def forgotpassword(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            emailid=form.cleaned_data.get('email')
            u = User.objects.get(email=emailid)
            print(u)
            password =random.randint(10000001,99999999)
            print(password)
            u.set_password(password)
            u.save()
            print(emailid)

            try:
                send_mail(
                    'Password changed',
                    render_to_string('auth/password_recover.html', {
                 'user': u,
                'password':password




             }),
                    'abhijitastlar@gmail.com',
                    [emailid],
                )
            except:

                return HttpResponse('Invalid email id . Doesnt exists')



            return HttpResponse('New Password sent to your email address.')
    else:
        form = PasswordForm()
    return render(request, 'auth/password_recovery.html', {'form': form})

