from django.db import models

# Create your models here.

class Category(models.Model):
    parent=models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE,related_name='sub')
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    def __str__(self):
        return self.title



class Size(models.Model):
    title=models.CharField(max_length=10)


    def __str__(self):
        return self.title


class Color(models.Model):
    title=models.CharField(max_length=30)



    def __str__(self):
        return  self.title

class Product(models.Model):
    category=models.ManyToManyField(Category,blank=True,null=True)
    title=models.CharField(max_length=55)
    description=models.TextField()
    price=models.IntegerField()
    discount=models.SmallIntegerField()
    image=models.ImageField(upload_to="product")
    size=models.ManyToManyField(Size,related_name="products",blank=True)
    color=models.ManyToManyField(Color,related_name="products")

    def __str__(self):
        return self.title

class Information(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="informations")
    text=models.TextField()

    def __str__(self):
        return self.text[:30]