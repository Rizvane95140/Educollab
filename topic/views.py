from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_discussion(request):
    context = {
        'page_title': 'Discussion'
    }
    
    context['user'] = request.user
    return render(request, 'topic/index.html', context)

