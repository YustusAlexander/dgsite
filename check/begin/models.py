from django.db import models

# Create your models here.
from django.urls import reverse


class Begin(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    number = models.IntegerField()
    photo = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('slug_url', kwargs={'slug_name': self.slug})

