from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from post.models import Post

from catalog.models import Catalog

def home(request):
    catalogs = Catalog.objects.all() 
    context = {"catalogs":catalogs}
    return render(request,"home.html",context)
   
def catadetail(request,pk):
    posts_cata = get_object_or_404(Catalog,pk=pk)
    posts = posts_cata.post_set.all()
    context = {"posts":posts,"catalog":posts_cata.name}
    return render(request,"home/cata-details.html",context)
