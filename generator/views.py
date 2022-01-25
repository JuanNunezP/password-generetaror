from pickletools import int4
from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def about(request): 
   return  render (request, 'about.html')
 
 
def home(request):
    
       return  render (request, 'home.html')

def password(request):
    
  characters= list('abcdefghijklmnopqrstuvwxyz')
  generate_password= "" 
    
  lenght = int(request.GET.get('length'))

  if request.GET.get('uppercase'):
     characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
       

  if request.GET.get ('special'):
     characters.extend(list('!#@$%*_-'))

  if request.GET.get('numbers'):
     characters.extend(list('0123456789'))

  for x in range(lenght):
    generate_password += random.choice(characters)
  
  return render(request,'password.html',{'password':generate_password})