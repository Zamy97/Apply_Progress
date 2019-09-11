from django.shortcuts import render

def index(request):
  return render(request, 'pages/home_view_index.html')
