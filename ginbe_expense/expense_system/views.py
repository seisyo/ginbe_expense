from django.shortcuts import render

def index(request):
    return render(request, 'expense_system/index.html')