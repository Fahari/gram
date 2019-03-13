from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .form import SignupForm

# Create your views here.
@login_required(login_url = "accounts/login")
def home(request):
    images=Image.objects.all()
    return render(request,'instagram.html',{"images":images})

def welcome(request):
    # images=Image.objects.all()
    if request.user.is_authenticated():
        return redirect('home')
    else:
        form = SignupForm()
    return render(request,'registration/login.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    pics = Image.objects.all()
    profile = Profile.objects.all()

    return render(request, 'registration/profile.html',locals())

def search_users(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, '/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
