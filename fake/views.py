from django.shortcuts import render
from django.http import HttpResponse
from .models import Test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import csv

# def home(request):
#     return HttpResponse('I"m here to start a new app')


class HomeView(ListView):
    model = Test
    template_name = 'fake/fake_list.html'
    

class TestCreate(CreateView):
    model = Test
    fields = '__all__'
    template_name = 'fake/fake_create.html'
    success_url = reverse_lazy('home')
    
    

class TestUpdate(UpdateView):
    model = Test
    fields = '__all__'
    template_name= 'fake/update.html'
    success_url = reverse_lazy('home')
    
class TestDelete(DeleteView):
    model = Test
    template_name= 'fake/fake_delete.html'
    success_url = reverse_lazy('home')
    

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    
    writer = csv.writer(response)
    writer.writerow(['User', 'Name', 'Job', 'Email', 'Age', 'Company', 'Updated time'])
    
    for element in Test.objects.all().values_list('user', 'name', 'job', 'email', 'age', 'company', 'created_at'):
        writer.writerow(element)
    response['Content-Disposition']= 'attachment; filename="fake_data.csv"'
    
    return response
    