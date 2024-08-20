from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
from .models import *
from django.contrib.sessions.backends.base import SessionBase
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def index(request):
    #print("products",product)
    contet = product.objects.all()
    #print(contet)
    print("Post Method ",request.POST)
    if request.method=='POST':
        prod_name = request.POST.get('filter')
        print("Product filet :- ",prod_name)
        if prod_name!='all':
            contet = product.objects.filter(product_choice=prod_name)
            top_pr = usb_product.objects.all()

        else:
            contet = product.objects.all()
            top_pr = usb_product.objects.all()

    else:
        contet = product.objects.all() 
        top_pr = usb_product.objects.all()
    context = {
        'contet':contet,    
        'top_pr':top_pr,
               }
    print("Top Products in context",context)
    return render(request,'index.html',context)


def products(request):
    contet = product.objects.all()
    print("products we have",contet)
    print("Post Method ",request.POST)
    if request.method=='POST':
        prod_name = request.POST.get('filter')
        print("Product filet :- ",prod_name)
        if prod_name!='All':
            contet = product.objects.filter(product_choice=prod_name)
            top_pr = usb_product.objects.all()
        else:
            print("Here is all")
            contet = product.objects.all()
            top_pr = usb_product.objects.all()

    else:
        contet = product.objects.all() 
        top_pr = usb_product.objects.all()
    context = {
        'contet':contet,    
        'top_pr':top_pr,
               }
    return render(request,'project.html',context)


def product_detail(request, slug):
    print("Hi in slug")
    prod = product.objects.filter(slug=slug).first()
    print("Slug product :- ", prod)
    context = {
        "product":prod,
    }

    return render(request,'productpage.html',context)

def suggest(request):
    pass


def about(request):
    print("about is here")
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')

def contacted(request):
    
    if request.method=="POST":
        name = request.POST.get('name')
        pnumber = request.POST.get('pnumber')
        email = request.POST.get('email')
        query = request.POST.get('query')

        fordet = contact(
            name= name,
            pnumber=pnumber,
            email = email,
            query = query,
        )

        fordet.save()

        return render(request,'index.html',{"Thanks":"Thanks for contacting us, we will reach you soon..."})
    else:
        return render(request,'index.html',{"Thanks":"Details are not submited, try again..."})