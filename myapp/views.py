from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request,pk):
    posts = Article.objects.get(id=pk)
    return render(request, 'post.html',{'posts':posts})