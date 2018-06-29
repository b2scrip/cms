from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from likedislike.models import LikeDislike
from post.models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect

class JoinFormView(View):
    template_name  = 'user/join_ajax.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
    def post(self, request, *args, **kwargs):
        print("posting..now")
        print(self.request.is_ajax())
        if not self.request.is_ajax():
            print("ajax calling ...")
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            user = authenticate(username=username, password=password)
            if user is not None:
                print("login.....ok...")
                login(request, user)
                data = {
                    'message':'ok'
                }
                return JsonResponse(data)
            else:
                data = {
                    'message':'nope'
                }
                return JsonResponse(data)
        else:
            return render(request, self.template_name, {})

class SignUpView(View):
    template_name  = 'user/signup_ajax.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{})
    def post(self, request, *args, **kwargs):
        print("about call ajax")
        if self.request.is_ajax():
            print("after check if ajax is calling...")
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            email = request.POST.get('email',None)
            print(username,password,email)
            if username is None or password is None or email is None:
                data = {
                    'message':'errorin'
                }
                return JsonResponse(data)

            reguser, created = User.objects.get_or_create(username=username)
            if created:
                reguser.set_password(password)
                reguser.email = email
                reguser.save()
                data = {
                    'message':'ok'
                }
                return JsonResponse(data)
            else:
                data = {
                    'message':'use'
                }
                return JsonResponse(data)
        else:
            return render(request, self.template_name, {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})

def user_posts_detail(request,id):
    author = get_object_or_404(User,pk=id)
    posts_list = author.post_set.all()
    paginator = Paginator(posts_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {"author":author,"userposts":posts}
    return render(request,"user/user-posts-all.html",context)

def user_posts_gallery(request,id):
    author = get_object_or_404(User,pk=id)
    gallery_list = author.picture_set.all()
    paginator = Paginator(gallery_list, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    gallerys = paginator.get_page(page)
    context = {"author":author,"gallerys":gallerys}
    return render(request,"user/user-posts-gallery.html",context)

@login_required
def user_profile(request):
    posts_list = request.user.post_set.all()
    paginator = Paginator(posts_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {"author":request.user,"userposts":posts}
    return render(request,"user/user-profile-posts.html",context)

@login_required
def profile_setting(request):
    pass 

def user_like_posts(request,id):
    author = get_object_or_404(User,pk=id)
    post_likes = [get_object_or_404(Post,pk=object_id["object_id"]) for object_id in author.likedislike_set.values("object_id")]
    context = {"postlikes":post_likes,"author":author}
    return render(request,"user/user-posts-likes.html",context)
