from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from service.models import Service

def home(request):
    
    return render(request,"home.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        Cpassword=request.POST.get("Cpassword")
        print(username,password)
        
        if User.objects.filter(username=username).exists():
            return render(request,"signup.html",{"error":"Username already exists"})
        
        
        
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()  # Ensure user is saved
            print("Debug: User created successfully!")  # Debugging message
            return redirect("login")  # Redirect to login page
        except Exception as e:
            print("Error:", e)  # Print error message
            return render(request, "signup.html", {"error": f"Error creating user: {str(e)}"})

    return render(request, "signup.html")
        
  
    

def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("dashboard")
        else:
            return render(request,"login.html",{"error":"Invalid credentials"})
         
    
    
    return render(request,"login.html")