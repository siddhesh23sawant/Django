from django.shortcuts import render, HttpResponse
from . models import Destination

# Create your views here.
def index(request):
    return render(request, 'index.html')


def courses(request):
    dests = Destination.objects.all()
    # dest3 = Destination()
    # dest3.name = 'MBlock'
    # dest3.img = 'mblock.png'
    # dest3.price = '500 INR'
    # dest3.desc = 'Drag & Drop'
    # dest3.offer = False
    # dests = [dest1, dest2, dest3]

    return render(request, "courses.html", {'dests': dests})

def search(request):
    query = request.GET['query']
    allpost = Destination.objects.filter(name__icontains=query)
    params= {'allpost': allpost}
    return render(request, 'search_result.html', params)
    # return HttpResponse("okay its working...")


def sorting(request):
    sorting = request.GET['sort_by']
    if sorting == 'name':
        dests = Destination.objects.order_by('name')

    elif sorting == 'price':
        dests = Destination.objects.order_by('price')

    elif sorting == '-price':
        dests = Destination.objects.order_by('-price')

    elif sorting == 'id':
        dests = Destination.objects.order_by('id')

    else:
        dests = Destination.objects.all()

    return render(request, "courses.html", {'dests': dests})


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog_details.html')


def element(request):
    return render(request, 'element.html')


def contact(request):
    return render(request, 'contact.html')