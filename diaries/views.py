from django.shortcuts import render, redirect

# Create your views here.
def index(request):
  return render(request, 'diaries/index.html')

def creatediary(request):
  pass

def mydiary(request):
  pass