from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes#, force_text
from .tokens import generate_token

from email.message import EmailMessage
from practice1 import settings


def home(request):
    return render(request, "authentication/index.html")     # request index page

def signup(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        username = request.POST['username']             # take data from signup page ...
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):      # check for username to match
            messages.error(request, "Username already exists! Please try some other username")
            return redirect('home')

        if User.objects.filter(email=email):            # check email
            messages.error(request,"Email already exists! Please try some other email")
            return redirect('home')

        if len(username) > 10:          # check for username criteria
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:              # match for password
            messages.error(request, "Password didn't match")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your Account had been Successfully Created \n We have send you confirmation Email \n Please confirm your email")     # Pass The Message


        # Welcome Email
        subject = "Welcome to First- Mail"
        message = "Hello" + myuser.first_name + "!! \n welcome to first one \n Thank you for visiting our side"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

    # Email Address Confitrmation

        current_site = get_current_site(request)
        email_subject = "Confirm your email firstone - Django Login "
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })

        # email Message send
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('signin')       # Back to sign In after create account

    return render(request, "authentication/signup.html")    # request signup page


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print("U:{0}".format(username))
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)       # check whether input user and pass match or not

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "authentication/signin.html")                   # request signin page

def signout(request):
    logout(request)
    messages.success(request, "Logges out successfully")
    return redirect('home')
    #return render(request, "authentication/sigout.html")

def activate(request, uibd64, token, force_text=None):
    try:
        uid = force_text(urlsafe_base64_decode(uibd64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request,'activation_failed.html')

