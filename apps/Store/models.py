from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    cate_id = models.IntegerField(primary_key=True, unique=True)
    cate_img = CloudinaryField('CateImg')
    cate_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.cate_name)
    

class Product(models.Model):
    prod_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=50, null=False)
    price = models.PositiveIntegerField(null=False)
    id_cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000,null=False)
    stock = models.PositiveIntegerField(null=False)
    img = CloudinaryField('ProdImg')
    insdate= models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "Codigo: {0} - Titulo: {1} - Autor {2} - Categoria: {3} - Stock: {4} - Fecha: {5}"
        return txt.format(self.prod_id, self.name, self.author, self.id_cate, self.stock, self.insdate)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    
    
    def __str__(self):
        return f"Cart {self.pk}"

    # Definir campo de clave primaria automático
    cart_id = models.AutoField(primary_key=True)
