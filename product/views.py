from django.shortcuts import render


def mainpage(request):
    return render(request,'product/mainpage.html')


def loginsign(request):
    return render(request, 'product/loginsign.html' )

def chatting(request):
    return render(request, 'product/chatting.html' )

def likecheck(request):
    return render(request, 'product/likecheck.html' )

def sign(request):
    return render(request, 'product/sign.html' )

def todaynews(request):
    return render(request, 'product/todaynews.html' )


# Create your views here.
