from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from sblog import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from .tokens import generate_token
from django.views import View
from .forms import PasswordForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
def login_form(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('appblog:index')
        else:
            return render(request,'accounts/login.html',{'invalid_login':True})
    return render(request,"accounts/login.html")
def logout_form(request):
    logout(request)
    return render(request,"accounts/login.html")
def register_form(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, 'Username Already Exist')
            return redirect('accounts:register')
        if User.objects.filter(email=email):
            messages.error(request, "This Email Already Registered")
            return redirect('accounts:register')
        if len(username)>18:
            messages.error(request, 'Username Must Be Under 18 Character')
            return redirect('accounts:register')
        if len(password)<8:
            messages.error(request, 'Password  Must Be More Then 8 Character ')
            return redirect('accounts:register')
            
        myuser = User.objects.create_user(username,email,password)
        myuser.is_active = False
        myuser.save()
        messages.success(request,"Your account Has Been Created, Please Check Your Email And Verify It")

        subject = "Welcome To Our Blog Website"
        message = "Hello " + myuser.username + "! \n" + "Thanks For Creating Account To Create Blogs\n Check The Other Email We Sent!"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)


        current_site = get_current_site(request)
        email_subject = "Confrim your email then you can login"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
 
        return redirect('accounts:login')
    return render(request, "accounts/signup.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        login(request,myuser)
        messages.success(request,"Your Account Got Active. Login!")
        return redirect('accounts:login')
    else:
        return render(request,"activation_failed.html")
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordForm
    success_url = reverse_lazy('password_sucess')
def password_sucess(request):
    return render(request,'accounts/password_sucess.html',{})