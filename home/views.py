from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    people = [{'Name':'Amit', 'Age':26},
              {'Name':'Vinay', 'Age':16},
              {'Name':'Prasad', 'Age':46},
              {'Name':'Vinod', 'Age':32},
              {'Name':'AJay', 'Age':62}
              ]
    return render(request, 'index.html', context={'peoples':people})
