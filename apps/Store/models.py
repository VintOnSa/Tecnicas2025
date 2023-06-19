from django.db import models

# Create your models here.

class Category(models.Model):
    cate_id = models.IntegerField(primary_key=True)
    cate_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.cate_name)
    

class Product(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    id_cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000,null=False)
    stock = models.IntegerField(null=False)
    img = models.ImageField(upload_to='ProdImg')
    insdate= models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "Codigo: {0} - Nombre: {1} - Categoria: {2} - Stock: {3} - Fecha: {4}"
        return txt.format(self.prod_id, self.name, self.id_cate, self.stock, self.insdate)
    