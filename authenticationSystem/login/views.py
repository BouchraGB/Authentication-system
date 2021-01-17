from django.shortcuts import render

from login.models import Users

# Create your views here.
def index(request):
    # Users.objects.all().delete()
    # user = Users(0,1,"bouchra","hello07")

    # user.save()

    # alll = Users.objects.all()
    # alll = alll.get()
    # alll = alll.password

    # print("hhhhhhhhhhhhhhhhhhhhh",alll)
    msg = False
    return render(request,'index.html',{'message':msg})


def check(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        hey = Users.objects.filter(username=username, password=password)
        if(hey.count() > 0 ):
            return render(request,'done.html',{'uu':username,'pp':password})

    # msg = "Account doesn't exisit, Try again"
    msg = True
    return render(request,'index.html',{'message':msg})
    
    


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = Users(0,1,username,password)
        user.save()
    return render(request,'done.html',{'uu':username,'pp':password})

def registerPage(request):

    return render(request,'register.html')