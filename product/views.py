from django.shortcuts import render


def mainpage(reqeust):
    return render(reqeust,'product/mainpage.html')

# Create your views here.
