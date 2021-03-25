from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from rest_framework.reverse import reverse


class Articles(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, related_name="articles")
    title = models.CharField('Title', max_length=500)
    text = models.TextField()
    moderation = models.BooleanField('Moderation', default=True)
    slug = models.SlugField(max_length=1000, unique=True, db_index=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-create']

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Articles, self).save(*args, **kwargs)
