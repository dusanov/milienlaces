from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Link, Client
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# TODO add LoginRequiredMixin
def index(request):
    context={}
    return render(request,'index.html',context=context)

class LinkCreate(LoginRequiredMixin, CreateView):
    model = Link
    fields = ['client', 'url', 'note', 'niche', 'link_type']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LinkUpdate(LoginRequiredMixin, UpdateView):
    model = Link
    fields = ['client', 'url', 'note', 'status', 'niche', 'link_type']

class LinkDelete(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('index')
