from django.shortcuts import render
from django.db.models.functions import Length
from app.models import *

# Create your views here.
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)
    

def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(Topic_Name='cricket')
    LWO=Webpage.objects.exclude(Topic_Name='Cricket')
    LWO=Webpage.objects.all()[2:5:]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.filter(Topic_Name='cricket').order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())

   
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)


def display_accessrecords(request):
    LAO=AccessRecords.objects.all()
    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d)