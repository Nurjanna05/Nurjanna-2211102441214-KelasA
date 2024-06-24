from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self) :
        return self.nama 

    class Meta:
        verbose_name_plural = "1. Kategori"

class Artikel(models.Model):
    judul = models.CharField(max_length=225)
    isi = models.TextField(blank=True, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    thumbnail = models.ImageField(upload_to='artikel', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=255)
    
    def __str__(self) :
        return self.judul 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super(Artikel, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "2. Artikel"