from django import forms
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from appblog.models import Post
class PasswordForm(PasswordChangeForm):
    old_password = forms.PasswordInput(attrs={'class':'input-field' })
    new_password1 = forms.PasswordInput(attrs={'class':'input-field' ,'id':'psw','name':'newpassword','placeholder':'new password'})
    new_password2 = forms.PasswordInput(attrs={'class':'input-field' ,'id':'psw','name':'newpassword1','placeholder':'confrim password'})
    class Meta:
        model = Post
        fields = ('old_password','new_password1','new_password2')