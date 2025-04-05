from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service  # Your Service model (URL shortening logic)
import random
import string

def generate_short_code():
    """Generate a random 6-character short code for the shortened URL."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
@login_required
def dashboard(request):
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        short_code = generate_short_code()  # Generate a random short code
        
        # Ensure short_code is unique
        while Service.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()
        
        # Create the shortened URL entry
        Service.objects.create(user=request.user, original_url=original_url, short_code=short_code)
        
        return redirect("dashboard")  # Redirect to the dashboard after shortening the URL

    # Fetch all URLs shortened by the logged-in user
    urls = Service.objects.filter(user=request.user)
    return render(request, "URL.html", {"urls": urls})

def redirect_url(request, short_code):
    """Redirect users from a short URL to the original URL."""
    # Get the Service object using the short_code.
    # If the short_code doesn't exist, it will raise a 404 error.
    url = get_object_or_404(Service, short_code=short_code)
    
    # Redirect the user to the original URL stored in the Service model.
    return redirect(url.original_url)


