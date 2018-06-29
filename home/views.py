from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from post.models import Post

from catalog.models import Catalog

def home(request):
    catalogs = Catalog.objects.all() 
    
    posts_list = Post.objects.all()

    paginator = Paginator(posts_list, 13)
    page = request.GET.get('page')
    posts =   paginator.get_page(page)

    context = {"catalogs":catalogs,"posts":posts}
    return render(request,"home.html",context)
   
def catadetail(request,pk):
    posts_cata = get_object_or_404(Catalog,pk=pk)
    posts = posts_cata.post_set.all()
    context = {"posts":posts}
    return render(request,"home/cata-details.html",context)
