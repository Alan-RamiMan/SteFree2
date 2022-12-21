from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    
Opcion_Consulta=[
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"],
]


class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    tipo_consulta=models.IntegerField(choices=Opcion_Consulta)
    mensaje=models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self) :
        return self.nombre