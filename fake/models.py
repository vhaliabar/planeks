from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(70), MinValueValidator(16)]
     )
    company = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")], 
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")
    
    class Meta:
        ordering = ['-name']
        
    @property
    def date_only(self):
        only_date = str(self.created_at.date())
        print(only_date)
        return 45

