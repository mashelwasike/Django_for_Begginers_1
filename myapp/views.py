from django.shortcuts import render
from . models import Article

# Create your views here.
def home(request):
    article = Article.objects.all().order_by('date')
    return render(request,'home.html', {'articles':article})

def about(request):
    return render(request,'about.html')

def details(request,slug):
    article = Article.objects.get(slug=slug) 
    return render(request,'details.html',{'article':article})