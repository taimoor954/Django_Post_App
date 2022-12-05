from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Posts
# Create your views here.
class HomePageView(TemplateView):
    template_name: str = "home.html"

    #This will be used to send data to html
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['my_thing'] = "Hello world coming from dynamic something"
        context['posts'] = Posts.objects.all()
        return context

class PostDetailView(DetailView):
    template_name: str ="detail.html"
    model = Posts

#https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/TemplateView/ for refrence