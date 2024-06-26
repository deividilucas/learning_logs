from django.shortcuts import render # type: ignore
from .models import Topic

# Create your views here.

def index(request):
    """" Página principal do Learning_Log"""
    return render(request, 'learning_logs/index.html')
    

def topics(request):
    """ Mostra todos os assuntos"""
    
    
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
    
    