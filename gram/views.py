from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import *
from .form import *

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


    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # message.success(request, f'Your account has been updated')
            return render(request,'registration/profile.html')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
            'u_form': u_form,
            'p_form': p_form

    }

    return render(request, 'registration/profile.html',locals())

def comment(request,image_id):
   current_user=request.user
   image = Image.objects.get(id=image_id)
   profile_user = User.objects.get(username=current_user)
   the_comments = Comment.objects.all()
   print(the_comments)
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
           comment_itself = form.save(commit=False)
           comment_itself.image = image
           comment_itself.commenter = request.user

           comment_itself.save()

           print(the_comments)


       return redirect(instagram)

   else:
       form = CommentForm()

   return render(request, 'comment.html', locals())


def search_users(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, '/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
