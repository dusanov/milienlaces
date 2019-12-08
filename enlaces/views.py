from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Link, Client
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

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

    def clean(self,form):
        print(' inside CLEAN ++++++++++++')
        parsedUrl = urlparse(self.url)
        insert = self.pk == None
        if insert:
            # load all links with the given netloc
            linksWithTheSameNetloc = Link.objects.filter(netloc=parsedUrl.netloc)
            for linkWithNetloc in linksWithTheSameNetloc:
                print('self.user = %(self.user)s',request.user)
                print('self.user = %(link.user)s',linkWithNetloc.user)
                if self.user == linkWithNetloc.user:
                    if linkWithNetloc.client == self.client and linkWithNetloc.link_type == self.link_type:
                        raise ValidationError(
                            {'url': ValidationError( 
                                _('Domain: %(domain)s for client %(client)s and link of type %(linkType)s is already in use'),
                                code='domain_in_use_1',
                                params={'domain':parsedUrl.netloc,
                                'client': self.client.name,
                                'linkType': self.get_link_type_display()}
                            )}
                        )
                else:
                    raise ValidationError(
                            {'url': ValidationError(
                                _('Domain %(domain)s already in use'),
                                code='domain_in_use_2',
                                params={'domain':parsedUrl.netloc}
                            )}
                    )
            self.netloc = parsedUrl.netloc
        else: print('it was update')

class LinkUpdate(LoginRequiredMixin, UpdateView):
    model = Link
    fields = ['client', 'url', 'note', 'status', 'niche', 'link_type']

class LinkDelete(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('index')
