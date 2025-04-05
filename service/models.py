from django.db import models
from django.contrib.auth.models import User
import random
import string

def generate_short_url():
    """Generate a random 6-character short URL code."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))

class Service(models.Model):  # Changed 'service' to 'Service' (PascalCase)
    """Model to store original URLs and their shortened versions."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link URL to a user
    original_url = models.URLField()  # Store the full URL
    short_code = models.CharField(max_length=6, unique=True, default=generate_short_url)  # Unique short URL code
    created_at = models.DateTimeField(auto_now_add=True)  # Store timestamp

    def get_short_url(self):  # Changed method name for better readability
        """Returns the full shortened URL (Change 'localhost' when deploying)."""
        return f"http://localhost:8000/{self.short_code}"

    def __str__(self):
        """String representation of the object (for admin panel & debugging)."""
        return f"{self.original_url} -> {self.get_short_url()}"
