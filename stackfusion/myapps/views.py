from django.shortcuts import render
from .models import Profile 
from django.contrib import messages 
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.urls import reverse 
from .serializers import ProfileSerializer
from rest_framework.parsers import JSONParser
import requests
from django.core.mail import send_mail 
from django.conf import settings 


# Create your views here.
def index(request):
    return render(request,'index.html')

def posts(request):
    if request.method == 'GET':
        posts = Profile.objects.all()
        serializer = ProfileSerializer(posts,many=True)
        return JsonResponse(serializer.data,safe=False)


def createdata(request):
    if request.method == 'POST':
        data1 = request.POST['username']
        data2 = request.POST['email']
        data3 = request.POST['dob']
        data4 = request.POST['age']
        data5 = request.POST['phone_no']
        converted_num = int(data4)
        converted_phone = int(data5) 
        
        # print(type(converted_num))
        # print('........') 
        x= len(data5)
        # print(x)
        # print(type(x))
        # print('.....') 

        
        
        if (converted_num < 18) :
            messages.info(request,"Age cannot be less than 18")
            return HttpResponseRedirect(reverse('index'))

        elif (converted_num >=18):
            if Profile.objects.filter(email=data2).exists():
                messages.info(request,"email already exist")
                return HttpResponseRedirect(reverse('index'))

            if (converted_phone < 0):
                messages.info(request,'Invalid Phone number')
                return HttpResponseRedirect(reverse('index'))

            if (x!=10):
                messages.info(request,"number must be 10 digit")
                return HttpResponseRedirect(reverse('index'))


            else:
                new_data = Profile(name=data1,email=data2,dob=data3,age=data4,phone_number=data5)
                
                new_data.save() 
                send_mail('This is the confirmation mail',data1,'settings.EMAIL_HOST_USER',[data2],fail_silently=False)
                return HttpResponseRedirect(reverse('home'))

            

    else:
        return render(request,'index.html')

def home(request):
    response = requests.get('http://127.0.0.1:8000/posts/').json()
    return render(request,'home.html',{'response':response})





        

        

            

