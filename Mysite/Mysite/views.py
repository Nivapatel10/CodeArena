from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,"login.html")
def dashboard(request):
    return render(request,"dashboard.html")
def signup(request):
    return render(request,"signup.html")
def login_view(request):
    return render(request,"login.html")
def profile(request):
    return render(request,"profile.html")