from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = "accounts/login")
def welcome(request):
    return render(request,'instagram.html')

def search_users(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, '/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
