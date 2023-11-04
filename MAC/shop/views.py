from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "shop/index.html")

def about(request):
    return HttpResponse("We r at about")

def contact(request):
    return HttpResponse("We r at contact")

def tracker(request):
    return HttpResponse("We r at tracker")

def search(request):
    return HttpResponse("We r at search")

def productView(request):
    return HttpResponse("We r at prodvuct view")

def checkout(request):
    return HttpResponse("We r at checkout")

#               QUIZ 
# def login(request):
#   return HttpResponse("We r at login")

# def signup(request):
#   return HttpResponse("We r at signup")



#            EXERCISE
# from .models import Product

#def index(request):
#    products = Product.objects.all()
#    context = {'products': products}
#    return render(request, 'shop/index.html', context)