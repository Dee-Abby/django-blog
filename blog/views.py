from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import( ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from .models import Chat



def home_page(request):
    context = {
        'posts' : Chat.objects.all()
    }
    return render(request, 'blog/home.html', context)

class ChatListView(ListView):
    model = Chat
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 5


    
class ChatDetailView(DetailView):
    model = Chat
    # fields = ['title', 'content']



class ChatCreateView(LoginRequiredMixin, CreateView):
    model = Chat
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        # validation of form
        return super().form_valid(form )
    

class ChatUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Chat
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        # validation of form
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class ChatDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Chat
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  

def about_page(request):
    return render(request, 'blog/about.html', {'title' : 'about'})


def favicon(request):
    return HttpResponse(status=204)