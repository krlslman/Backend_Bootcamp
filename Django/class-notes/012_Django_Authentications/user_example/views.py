from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")

def register(request):
    # form = UserCreationForm()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    ## Bu 3 satır yerine aşağıdaki tek satır kod aynı işi yapıyor;
   
    #? pass in post data when instantiate the form
    form = UserCreationForm(request.POST or None)
    #? if the form is ok with the info filled:
    if form.is_valid():
        form.save()
        #? that creates a new user
        #? after creation of the user, want to authenticate it
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        #? inspect the page and see the first password is password1, import authenticate
        user = authenticate(username=username, password=password)
        #? want user to login right after registered, import login

        login(request, user)
        #? want to redirect to home page, import redirect
        return redirect("login")

    contex = {
        'form':form
    }

    return render(request, 'registration/register.html', contex)