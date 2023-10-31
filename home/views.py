from django.shortcuts import render

# Create your views here.


def index(request):
    """ Return the index page """

    return render(request, 'home/index.html')


def about_us(request):
    """ Return to About Us """
    return render(request, 'home/about_us.html')


def gallery(request):
    """ Return to Gallery """
    return render(request, 'home/gallery.html')


def reviews(request):
    """ Return to Reviews """
    return render(request, 'home/reviews.html')


def walking_packages(request):
    """ Return to Walking Packages """
    return render(request, 'home/walking_packages.html')