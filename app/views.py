from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)
    

def display_webpages(request):
    LWO=Webpage.objects.all()
    d1={'LWO':LWO}
    return render(request,'display_webpages.html',d1)


def display_accessrecords(request):
    LAO=AccessRecords.objects.all()
    d3={'LAO':LAO}
    return render(request,'display_accessrecords.html',d3)