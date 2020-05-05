from django.shortcuts import render

def AccountHome(request):
    return render(request, 'user_system/account_home.html')

