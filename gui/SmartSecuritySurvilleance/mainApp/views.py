from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'mainApp/index.html')

def addNew(request):
	return render(request, 'mainApp/addNew.html')