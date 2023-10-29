import requests
from django.http import HttpResponseRedirect

from .models import Links
from bs4 import  BeautifulSoup
from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method=="POST":
        new_link=request.POST.get('page')
        urls=requests.get(new_link)
        beautysoup=BeautifulSoup(urls.text,'html.parser')

        for link in beautysoup.find_all('a'):
            address=link.get('href')
            name=link.string
            Links.objects.create(address=address,stringname=name)
            return HttpResponseRedirect('/')
    else:
        datavalue=Links.objects.all()

    return  render(request,'home.html',{'datavalue':datavalue})
