from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import csv

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# def home(request):
#     return HttpResponse('I"m here to start a new app')

class CustomLoginView(LoginView):
    template_name = 'fake/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')

class HomeView(LoginRequiredMixin, ListView):
    model = Test
    template_name = 'fake/fake_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context
    

class TestCreate(LoginRequiredMixin, CreateView):
    model = Test
    fields = ['name', 'job', 'email', 'age', 'company']
    template_name = 'fake/fake_create.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TestCreate, self).form_valid(form)
    
    

class TestUpdate(LoginRequiredMixin, UpdateView):
    model = Test
    fields = ['name', 'job', 'email', 'age', 'company']
    template_name= 'fake/update.html'
    success_url = reverse_lazy('home')
    
class TestDelete(LoginRequiredMixin, DeleteView):
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
    