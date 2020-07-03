from django.shortcuts import render
from mysite.models import contact,quotes,sayings
import requests
import random



def index(request):
    if request.method=="POST":
        
        totentries=len(sayings.objects.all())
        qno=random.randint(1,totentries+1)
        print(qno)
        rsaying=sayings.objects.all()[qno-1]

        
        context={'rsaying':rsaying}
        print(context)
        return render(request,'mysite/index.html',context)
    else:
 
        
        totentries=len(sayings.objects.all())
        qno=random.randint(1,totentries+1)
        print(qno)
        rsaying=sayings.objects.all()[qno-1]

        
        context={'rsaying':rsaying}
        print(context)
        return render(request,'mysite/index.html',context)

def portfolio(request):


    totalentries=quotes.objects.all().count()
    
    randomlist=[]
    randomlist=random.sample(range(1,totalentries+1), 9)
    



    id1=randomlist[0]
    
    rquote=quotes.objects.all()[id1-1   ]
    




    id2=randomlist[1]
    
    r1quote=quotes.objects.all()[id2-1]
    



    id3=randomlist[2]
    
    r2quote=quotes.objects.all()[id3-1]
    




    id4=randomlist[3]
    
    r3quote=quotes.objects.all()[id4-1]
    



    id5=randomlist[4]
    
    r4quote=quotes.objects.all()[id5-1]
    



    id6=randomlist[5]
    
    r5quote=quotes.objects.all()[id6-1]
    





    id7=randomlist[6]
    
    r6quote=quotes.objects.all()[id7-1]
    



    id8=randomlist[7]
    
    r7quote=quotes.objects.all()[id8-1]
    




    id9=randomlist[8]
    
    r8quote=quotes.objects.all()[id9-1]
    

    contexts={'rquote':rquote,'r1quote':r1quote,'r2quote':r2quote,'r3quote':r3quote,'r4quote':r4quote,'r5quote':r5quote,'r6quote':r6quote,'r7quote':r7quote,'r8quote':r8quote}
    print(contexts)

    
    

    

    return render(request,'mysite/portfolio.html',contexts)

def contactme(request):
    if request.method=="POST":
        email= request.POST['email']
        subject= request.POST['subject']
        message= request.POST["message"]
        
        c = contact.objects.create(email=email, subject= subject, message= message)
        c.save()
        return render(request,'mysite/thank.html')
    else:
        return render(request,'mysite/contact.html')

        