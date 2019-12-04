from django.db import models
from django.contrib.auth.models import User

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

# add a field for delete: status or delted or something
class Link(models.Model):
    def __str__(self): return f'{self.url}'
    # TODO check if on delete is correct
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    url = models.URLField(blank=False)
    note = models.TextField(blank=True)
    date_created = models.DateField("date created", auto_now_add=True)
    date_modified = models.DateField("date modified", auto_now_add=True)
    quality = models.PositiveSmallIntegerField
    target = models.URLField
    LINK_STATUS = (
        ('o','opportunity'),
        ('d','declined'),
        ('r','requested'),
        ('p','pending'),
        ('c','confirmed'),
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
