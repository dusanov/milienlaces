from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlparse
from django.contrib.auth.mixins import LoginRequiredMixin

class Client(models.Model):
    name = models.CharField(max_length=50, blank=False)
    domain = models.URLField(blank=False)
    CLIENT_STATUS = (
        ('a', 'Active'),
        ('h', 'On Hold')
    )
    status = models.CharField(
            max_length=1,
            choices=CLIENT_STATUS,
            blank=False,
            default='a')

    class Meta: ordering = ['name']
    def __str__(self): return f'{self.domain}'

class Link(models.Model, LoginRequiredMixin):
    readonly_fields = ["netloc"]
    def validateURL(url):return True # legacy migration shit
    """
    def clean(self):
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
    """
    netloc = models.CharField(max_length=50, blank=False, default='')
    # TODO check if on delete is correct
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    url = models.URLField(blank=False,validators=[validateURL])
    note = models.TextField(blank=True)
    date_created = models.DateField("date created", auto_now_add=True)
    date_modified = models.DateField("date modified", auto_now_add=True)
    quality = models.PositiveSmallIntegerField
    target = models.URLField
    LINK_STATUS = (
        ('o','opportunity'),
        ('r','requested'),
        ('p','pending'),
        ('c','confirmed'),
        ('d','declined'),
        ('d','deleted')
    )
    status = models.CharField(
            max_length=1,
            choices=LINK_STATUS,
            blank=False,
            default='o')
    LINK_NICHE = (
        ('biz', 'business'),
        ('lfs', 'lifestyle'),
        ('hmi', 'home improvement'), 
        ('eco', 'green'), 
        ('tra', 'travel'), 
        ('fml', 'family'), 
        ('dsg', 'design'), 
        ('mrk', 'marketing'), 
        ('tch', 'tech'), 
        ('edu', 'education'), 
        ('car', 'auto'), 
        ('hlt', 'health & beauty'),
        ('oth', 'other')
    )
    LINK_TYPE = (
        ('g','guest post'),
        ('p','paid post'),
        ('b','blog comment'),
        ('c','citation'),
        ('f','forum'),
        ('o','other')
    )
    niche = models.CharField(
            max_length=3,
            choices=LINK_NICHE,
            blank=False)
    link_type = models.CharField(
            max_length=1,
            choices=LINK_TYPE,
            blank=False)
    def __str__(self): return f'{self.url}'
