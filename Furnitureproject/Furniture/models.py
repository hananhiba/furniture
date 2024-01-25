from django.db import models
from django.urls import reverse


# Create your models here.

class Furniture(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='furniture',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='furniture'
        verbose_name_plural = 'furniture'

    def get_url(self):
        return reverse('Furniture:Product_by_Category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Furniture,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField(blank=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('Furniture:ProductDetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)
