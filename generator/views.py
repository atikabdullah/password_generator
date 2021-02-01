from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,"generator/home.html")
# def prac(reqest):
#     return HttpResponse("{'name':'Atk_Abdullah'}")
def password(request):
    characters=list('')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'))
    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))



    length = int(request.GET.get('length',12))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})
