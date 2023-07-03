from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import datas

# Create your views here.
def demo(request):
    obj=place.objects.all()
    dat=datas.objects.all()
    return render(request,'index.html',{'res':obj,'resu':dat})