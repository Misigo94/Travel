from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Image,Category
from django.contrib import messages
from django.db.models import Q, query

# Create your views here.
def index(request):
    img = Image.objects.all()
    # category=Image.objects.filter(Category = 'food')
    # q1 = Entry.objects.filter(headline__startswith="What")

    return render(request, 'index.html',{'img':img})

# def search(request):
#     query = None
#     result = []
#     if request.method == 'GET':
#         query = request.GET.get('search')
#         result = Image.objects.filter(Q(title__icontains=query))
#     return render(request, 'search.html',{'result': result},{'query': query})

def search(request):

    if 'category' in request.GET and request.GET['category']:
        search_images = request.GET.get("category")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

