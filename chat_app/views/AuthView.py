from django.shortcuts import render, redirect
from chat_app.forms import SignUpForm
from django.contrib.auth.models import User

def login_redirect(request):
    if request.user.is_authenticated():
        return redirect('/messenger')
    else:
        return redirect('/login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignUpForm()
        args = {'form' : form}
        return render(request, 'chat_app/signup.html', args)



