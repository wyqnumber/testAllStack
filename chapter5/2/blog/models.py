# coding=utf-8
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blog_plural')

    title = models.CharField(max_length=30, unique=True, verbose_name=_('title'), help_text='blogs title')
    author = models.ForeignKey(User, verbose_name=_('author'))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_('URL'))
    body = models.TextField(verbose_name=_('content'))
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '%s' % (self.title)

    @permalink
    def get_absolute_url(self):
        return 'blog_view', None, {'slug': self.slug}
