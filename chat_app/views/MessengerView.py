from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def index(request):
    args = {'user': request.user}
    return render(request, 'chat_app/messenger.html', args)
