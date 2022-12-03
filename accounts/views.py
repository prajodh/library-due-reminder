

from multiprocessing import AuthenticationError

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from .models import library_db


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        libList = library_db.objects.all()
        if user is not None:
            auth.login(request,user)
            return render(request,'data.html',{'username':username,'libList':libList})
    return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        # user = authenticate(username = username)
        if User.objects.filter(username=username).exists():
            return redirect(request,'signup')
            
        else:
            user = User.objects.create_user(username = username,password = password,email = email)
            user.save();
            return render(request,'login.html')


    return render(request,'signup.html')    

def booklist(request):
    return render(request,'data.html')

def books(request):
    l = library_db()
    if request.method == 'POST':
        l.username = request.POST['username']
        username = request.POST['username']
        l.libraryId = request.POST['libraryId']
        l.bookTitle = request.POST['bookTitle']
        l.dateOut = request.POST['dateOut']
        l.dueDate = request.POST['dueDate']
        l.due = request.POST['due']
        l.save();
        libList = library_db.objects.all()
        return render(request,'data.html',{'username':username,'libList':libList} )



    return render(request,'books.html')

