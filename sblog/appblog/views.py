from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Post,Category,usrpfp,Comment
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.core.mail import send_mail
from sblog import settings
from django.views import View
from .forms import PostBlog,EditPost,ProfileEdit,ProfilePageForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
class Index(ListView):
    model = Post
    template_name = 'appblog/index.html'
    ordering = ['-create_at']
    def get_context_data(self, *args,**kwargs):
        list_category = Category.objects.all()
        context = super(Index,self).get_context_data(*args,**kwargs)   
        context['list_category'] = list_category
        return context
class ArticleView(DetailView):
    model = Post
    template_name = "appblog/article_detailes.html"

    def get_context_data(self, *args,**kwargs):
        list_category = Category.objects.all()
        context = super(ArticleView,self).get_context_data(*args,**kwargs)   
        like = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = like.total_likes()

        liked = False
        if like.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['list_category'] = list_category
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        if request.user.is_authenticated:
            text = request.POST.get('comment')
            if text:
                comment = Comment(post=post, user=request.user, text=text)
                comment.save()

        return redirect('appblog:article-detail', pk=post.pk, name=post.title)
class AddPost(CreateView):
    model = Post
    form_class = PostBlog
    template_name = "appblog/apost.html"
class Edit(UpdateView):
    model = Post
    form_class = EditPost
    template_name = "appblog/update.html"

class CategoryView(CreateView):
    model = Category
    template_name = "appblog/create_category.html"
    fields = "__all__"
def CategoryListViw(request):
    category_menu = Category.objects.all()
    return render(request,'appblog/category_menu.html',{'category_menu':category_menu})    

#------------

def CategoryList(request,list):
    category_posts = Post.objects.filter(category=list.replace('-',' '))
    return render(request,'appblog/category_list.html',{'list':list.title().replace('-',' '),'category_posts':category_posts})
class Delete(DeleteView):
    model = Post
    template_name = "appblog/delete.html"
    success_url = reverse_lazy('appblog:index')
def LikePost(request, pk, name):
    post = get_object_or_404(Post, id=pk)   
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    url = reverse('appblog:article-detail', args=[str(pk), name])
    return HttpResponseRedirect(url)
class ProfileEdit(generic.UpdateView):
    form_class = ProfileEdit
    template_name = 'appblog/profile_edit.html'
    success_url = reverse_lazy('appblog:index')
    
    def get_object(self):
        return self.request.user
    
class ProfilePage(DetailView):
    model = usrpfp
    template_name = 'appblog/profile.html'
    context_object_name = 'usr_page'

    def get_object(self, queryset=None):
        return get_object_or_404(usrpfp, user__username=self.kwargs['username'])

    def get_context_data(self, *args, **kwargs):
        usr_page = self.get_object()
        user_posts = Post.objects.filter(author=usr_page.user)
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        context['user_posts'] = user_posts
        return context

class CreateProfilePage(generic.CreateView, ProfilePageForm):
    model = usrpfp
    form_class = ProfilePageForm
    template_name = 'appblog/create_profile_page.html'

    def form_valid(self, form):
        existing_profile = usrpfp.objects.filter(user=self.request.user).first()

        if existing_profile:
            existing_profile.bio = form.cleaned_data['bio']
            existing_profile.profile = form.cleaned_data['profile']
            existing_profile.website_url = form.cleaned_data['website_url']
            existing_profile.github_url = form.cleaned_data['github_url']
            existing_profile.twitter_url = form.cleaned_data['twitter_url']
            existing_profile.instagram_url = form.cleaned_data['instagram_url']
            existing_profile.save()
        else:
            form.instance.user = self.request.user
            form.save()

        return super().form_valid(form)
    
class EditProfilePage(generic.UpdateView):
    model = usrpfp
    fields = ['bio','profile','website_url','github_url','twitter_url','instagram_url']
    template_name = 'appblog/edit_profile_page.html'
    success_url = reverse_lazy('appblog:index')
class DeleteCommentView(View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user == comment.user:
            comment.delete()

        return redirect('appblog:article-detail', pk=comment.post.pk, name=comment.post.title)

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            try:
                subject = f"Contact Request from {name} ({email}d)"
                send_mail(
                    subject,
                    message,
                    email,
                    ['gacradin@gmail.com'],
                    fail_silently=False
                )
                return render(request,'appblog/index.html')
            except Exception as e:
                return HttpResponse('An error occurred while sending the email: ' + str(e))
        else:
            return HttpResponse('Please fill in all required fields.')

    return render(request, "appblog/index.html")