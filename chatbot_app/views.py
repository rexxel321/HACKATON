from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def tickets(request):
    return render(request, 'tickets.html')

def contact(request):
    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def syarat_ketentuan(request):
    return render(request, 'syarat ketentuan.html')

def login(request):
    return render(request, 'login.html')

def kereta(request):
    return render(request, 'kereta.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def tentang_kami(request):  # Kalau ada halaman ini
    return render(request, 'tentang_kami.html')

