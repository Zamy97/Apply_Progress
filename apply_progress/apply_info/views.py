from django.shortcuts import render

def index(request):
    return render(request, 'apply_info/apply_info_index.html')
