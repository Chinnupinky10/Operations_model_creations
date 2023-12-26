from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models import Q
def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(len('name'))
    QLWO=Webpage.objects.all().order_by(len('name').desc())
    QLWO=Webpage.objects.all()[:5:]
    QLWO=Webpage.objects.all()[2:5:]
    QLWO=Webpage.objects.filter(name__startswith='r')
    QLWO=Webpage.objects.filter(name__endswith='t')
    QLWO=Webpage.objects.filter(name__contains='r')
    QLWO=Webpage.objects.filter(name__regex='\w+t$')
    QLWO=Webpage.objects.filter(topic_name='cricket',name__startswith='R')
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') | Q(name__startswith='R'))
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') & Q(name__startswith='R'))
    QLWO=Webpage.objects.filter(topic_name='cricket').order_by('name')
    QLWO=Webpage.objects.filter(topic_name='cricket').order_by('-name')
    QLWO=Webpage.objects.filter(topic_name='cricket').order_by(len('name'))
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)
    

def display_accessrecords(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(id__lte=4)
    QLAO=AccessRecord.objects.filter(date__lt='2023-12-19')
    QLAO=AccessRecord.objects.filter(date='2023-12-18')
    QLAO=AccessRecord.objects.filter(date__gt='2023-12-19')
    QLAO=AccessRecord.objects.filter(pk__in=(3,6))
    d={'AccessRecords':QLAO}
    return render(request,'display_accessrecords.html',d)


def insert_topic(request):
    tn=input('enter tn')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return HttpResponse('Topic is inserted')


def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    TO=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()
    return HttpResponse('webpage is created')

def insert_access(request):
    pk=int(input('enter pk value of webpage'))
    a=input('enter author')
    d=input('enter date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    return HttpResponse('Access is created')



def update_webpage(request):
    #webpage.objects.filter(topic_name='cricket').update(name='Rohit Sharma')

    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)




    





