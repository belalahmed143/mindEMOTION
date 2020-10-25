from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    carousels = Carousel.objects.all()
    videos = Video.objects.all().order_by('-date')[:9]


    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        submit = Contact(name=name, email=email, phone=phone ,subject=subject,message=message)
        messages.success(request, 'successfully submit')
        submit.save()
        return redirect('index')
        
    context={
        'videos':videos,
        'carousels':carousels
    }
    return render(request, 'index.html',context)

def Videos(request):
    videoss=Video.objects.all().order_by('-date')
    return render(request,'video.html',{'videoss':videoss})

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')
        
        if query is not None:
            lookups=Q(name__icontains=query)
            post= Video.objects.filter(lookups).distinct()

            context ={
                'post':post,
                'submitbutton':submitbutton
            }
            return render(request,'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')

