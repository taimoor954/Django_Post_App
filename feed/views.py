from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView
from .models import Posts
from .forms import PostForm
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

class AddPostImageView(FormView):
    template_name: str ="form.html"
    success_url = '/home'
    form_class = PostForm

    def form_valid(self, form):
        print('This was valid')
        print(form.cleaned_data['text'])
        print(form.cleaned_data['text'])
        print(form.cleaned_data['text'])
        print(form.cleaned_data['text'])
        print(form.cleaned_data['text'])
        new_object = Posts.objects.create(text=form.cleaned_data['text'], image= form.cleaned_data['image'])
        return super().form_valid(form)

#https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/TemplateView/ for refrence