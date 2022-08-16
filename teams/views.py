from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Team, TeamMember
from django.conf import settings
from django.core.mail import send_mail
import uuid

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    if request.method == "POST":
        #Handle team members form
        firstName = request.POST['fname']
        lastName = request.POST['lname']     
        email = request.POST['signUpEmail']


    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('/')

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.error(request, 'User not found')
            return redirect('/login')
        team_obj = Team.objects.filter(user=user_obj).first()
        if not team_obj.is_verified:
            messages.info(request, 'Profile is not verified yet. Please check your mail')
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Wrong password or username')
            return redirect('/login')
        login(request, user)
        return redirect('/dashboard')
    return render(request , 'login.html')

def handleLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect('/')
    else:
        return HttpResponse("404 - Page not found")

def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        team_name = request.POST.get('team_name')
        try:
            if User.objects.filter(username=username).first():
                messages.warning(request, 'Username is already taken')
                return redirect('/signup')
            if User.objects.filter(email=email).first():
                messages.warning(request, 'Email is already taken.')
                return redirect('/signup')
            if password1 != password2:
                messages.warning(request, 'Passwords do not match')
                return redirect('/signup')
            user =  User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            auth_token = str(uuid.uuid4())
            team = Team(user=user, auth_token=auth_token, team_name=team_name)
            team.save()
            sendMail(email, auth_token)
            return redirect('/token')
        except Exception as e:
            messages.error(request, 'Error occured')
            return redirect('/')
    else:
        return render(request, 'signup.html')

def token(request):
    return render(request, 'token.html')

def sendMail(email, token):
    subject = 'Verify your account - Hult Prize'
    message = f'Please click the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):
    try:
        team_obj = Team.objects.filter(auth_token=auth_token).first()
        if team_obj:
            if team_obj.is_verified:
                messages.success(request, 'Your account is already verified')
                return redirect('/')
            team_obj.is_verified = True
            team_obj.save()
            messages.success(request, 'Your account has been verified')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        return redirect('/')

def error(request):
    return  render(request, 'error.html')
