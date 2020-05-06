from django.shortcuts import render

def index(request):
    return render(request, 'expense_system/index.html')

def input(request):
    return render(request, 'expense_system/input.html')