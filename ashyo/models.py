from django.db import models


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

class Client(BaseModel):
  class clientPayChoices(models.TextChoices):
     NAQD = "naqd", "Naqd"
     KREDIT = "kredit", "Kredit"
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  phone = models.CharField(max_length=50)
  email = models.EmailField()
  pay = models.CharField(max_length=55, choices=clientPayChoices.choices, default=clientPayChoices.NAQD)
  pasport_img = models.ImageField(upload_to="pasport")




class Category(BaseModel):
   name = models.CharField(max_length=100)
   icon = models.ImageField(upload_to='category_icon')

class Characteristics(BaseModel):
   model = models.CharField(max_length=50)
   brend = models.CharField(max_length=50)
   size = models.CharField(max_length=50, null=True)
   accumulator = models.CharField(max_length=50, null=True)
   ram = models.CharField(max_length=50, null=True)
   rom = models.CharField(max_length=50, null=True)
   processor = models.CharField(max_length=50, null=True)
   simcard = models.CharField(max_length=50, null=True)
   core = models.CharField(max_length=50, null=True)



class Product(BaseModel):
  name = models.CharField(max_length=200)
  price = models.DecimalField(decimal_places=2)
  img = models.ImageField(upload_to="image")
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.PROTECT )
  character = models.ForeignKey(Characteristics, on_delete=models.PROTECT )
 
class Brend(BaseModel):
   name = models.CharField(max_length=50)
   add_price = models.DecimalField(max_digits=10, decimal_places=10)
   product = models.ForeignKey(Product, on_delete=models.PROTECT)
   img = models.ImageField(upload_to='brend')

class ProductMemory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    add_price = models.DecimalField(max_digits=10, decimal_places=10)
    memory = models.CharField(max_length=100)

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    color = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='products/')
    image_2 = models.ImageField(upload_to='products/')
    image_3 = models.ImageField(upload_to='products/')
    add_price = models.DecimalField(max_digits=10, decimal_places=10)

class AboutAshyo(BaseModel):
   title = models.CharField(max_length=200)
   img = models.ImageField(upload_to="Ashyo")
   description = models.TextField()

class Comment(BaseModel):
   comment = models.TextField()
   product = models.ForeignKey(Product,on_delete=models.PROTECT)
   client = models.ForeignKey(Client, on_delete=models.PROTECT)
   rate = models.PositiveIntegerField()

class ProductInCart(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    product_color = models.ForeignKey(ProductImages, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductMemory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey('shop.Order', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.id}-{self.product}"
   
   


  
  
