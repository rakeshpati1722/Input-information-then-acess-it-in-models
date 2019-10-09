from django.shortcuts import render
from app.forms import NewUser
# Create your views here.

def user(request):
    form = NewUser
    
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return user(request)
        else:
            print("Error ")
    return render (request, 'index.html',{'form':form})

        