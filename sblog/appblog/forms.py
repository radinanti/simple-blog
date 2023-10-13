from django import forms
from .models import Post,Category,usrpfp
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
choose = Category.objects.all().values_list('name','name')
category_list = []
for i in choose:
    category_list.append(i)
class PostBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','header_image',f'title_tag','author','category','text')
        widgets = {
            'title': forms.TextInput(attrs={'class':'input-form', 'placeholder': 'title'}),
            'title_tag':forms.TextInput(attrs={'class':'input-form', 'placeholder': 'title_tag'}),
            'author':forms.TextInput(attrs={'class':'input-form','value':'','id':'userid','type':'hidden'}),
            'category':forms.Select(choices=category_list,attrs={'class':'input-form'}),
            'text':forms.Textarea(attrs={'class':'input-form', 'placeholder': 'text'})
        
        
        
        }   
class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','header_image','category','text')
        widgets = {
            'title': forms.TextInput(attrs={'class':'input-form', 'placeholder': 'title'}),
            'title_tag':forms.TextInput(attrs={'class':'input-form', 'placeholder': 'title_tag'}),
            'category':forms.Select(choices=category_list,attrs={'class':''}),
            'text':forms.Textarea(attrs={'class':'input-form', 'placeholder': 'text'})
        
        
        
        }           
class ProfileEdit(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_login','date_joined']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field'}),
            'email': forms.EmailInput(attrs={'class': 'input-field'}),
            'last_login': forms.TextInput(attrs={'class': 'input-field', 'disabled': 'true'}),
            'date_joined': forms.TextInput(attrs={'class': 'input-field', 'disabled': 'true'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['last_login'].required = False
        self.fields['date_joined'].required = False    
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = usrpfp
        fields = ('bio','profile','website_url','github_url','twitter_url','instagram_url')
        widgets ={
            'bio': forms.Textarea(attrs={'class':'input-form', 'placeholder': 'title'}),
            'website_url':forms.TextInput(attrs={'class':'input-form','placeholder':'website link'}),
            'github_url':forms.TextInput(attrs={'class':'input-form', 'placeholder': 'github link'}),
            'twitter_url':forms.TextInput(attrs={'class':'input-form', 'placeholder': 'twitter link'}),
            'instagram_url':forms.TextInput(attrs={'class':'input-form', 'placeholder': 'instagram link'}),
            
        
    }