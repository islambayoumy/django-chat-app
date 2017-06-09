from django.shortcuts import render

def test(request):
    return render(request, 'chat_app/login.html')
