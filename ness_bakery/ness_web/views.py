from django.shortcuts import render
from .models import *
from subprocess import run, PIPE
import sys


# Create your views here.
def home(request):
    get_portfolio = Portfolio.objects.all()
    get_testimony = Testimonial.objects.all()
    get_blog = Blog.objects.all()
    get_product = Product.objects.all()
    get_gc = GraduationCake.objects.all()
    get_tc = ThemedCake.objects.all()
    get_bc = BirthdayCake.objects.all()
    get_bsc = BabyShowerCake.objects.all()
    get_wc = WeddingCake.objects.all()
    get_cc = CupCake.objects.all()

    context = {
        'get_portfolio': get_portfolio,
        'get_testimony': get_testimony,
        'get_blog': get_blog,
        'get_product': get_product,
        'get_gc': get_gc,
        'get_tc': get_tc,
        'get_bc': get_bc,
        'get_bsc': get_bsc,
        'get_wc': get_wc,
        'get_cc': get_cc,
    }
    return render(request, 'ness_web/index.html', context)


def mpesa(request):
    inp = request.POST.get('price')
    output = run(sys.executable, ['//mpesa_api//lipanampesa.py'], shell = False, stdout=PIPE)
    return render(request, 'ness_web/index.html', {'data':output})


""""
def portfolio(request):
    get_portfolio = Portfolio.objects.all()
    context = {
        'get_portfolio': get_portfolio,
               }

    return render(request, 'ness_web/index.html', context)


def testimony(request):
    get_testimony = Testimonial.objects.all()
    context = {
        'get_testimony': get_testimony
    }
    return render(request, 'ness_web/index.html', context)


def blog(request):
    get_blog = Blog.objects.all()
    context = {
        'get_blog': get_blog
    }
    return render(request, 'ness_web/index.html', context) """""
