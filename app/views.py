from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Notice
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class listview(ListView):
    model = Notice
    template_name = 'app/notice_list.html'
    context_object_name = 'notices'
    
@method_decorator(login_required,name='dispatch')
class detailview(DetailView):
    model = Notice
    template_name = 'app/detail.html'
    context_object_name = 'notices'