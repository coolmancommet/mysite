from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin




def home(request):
    content={'post':post.objects.all() }
    return render(request,'blog/home.html',content)

class PostListView(ListView):
    model=post
    template_name='blog/home.html'#<app>/<model>_<viewtype>.htlm
    context_object_name='post'
    ordering =['-date_posted']


class PostCreateView(LoginRequiredMixin,CreateView):
    model=post
    fields=['title','content','image']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields=['title','content','image']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False


class PostDetailView(DetailView):
    model=post



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    success_url='/profile'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False



def about(request):
    return HttpResponse('<h2> bblog-abut </h2>')
