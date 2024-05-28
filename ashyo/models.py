from django.db import models


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

class Client(BaseModel):
  full_name = models.CharField(max_length=100)
  phone = models.CharField(max_length=50)
  email = models.EmailField()

class Category(BaseModel):
   name = models.CharField(max_length=100)
   icon = models.ImageField(upload_to='category_icon')

class Characteristics(BaseModel):
   model = models.CharField(max_length=50)
   brend = models.CharField(max_length=50)
   size = models.CharField(max_length=50)
   accumulator = models.CharField(max_length=50)
   ram = models.CharField(max_length=50)
   rom = models.CharField(max_length=50)
   processor = models.CharField(max_length=50)
   simcard = models.CharField(max_length=50)
   core = models.CharField(max_length=50)



class Product(BaseModel):
  name = models.CharField(max_length=200)
  price = models.DecimalField(decimal_places=2)
  img = models.ImageField(upload_to="image")
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.PROTECT )
  character = models.ForeignKey(Characteristics, on_delete=models.PROTECT )
 

class Comment(BaseModel):
   comment = models.TextField()
   product = models.ForeignKey(Product,on_delete=models.PROTECT)
   client = models.ForeignKey(Client, on_delete=models.PROTECT)
   rate = models.PositiveIntegerField()


   
   


  
  
