from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True



class PymentType(models.Model):
    cart = models.CharField(max_length=50)
    cash = models.CharField(max_length=50)
    credit = models.CharField(max_length=50)


class CreditImage(BaseModel):

    image_1 = models.ImageField(upload_to='media/')
    image_2 = models.ImageField(upload_to='media/')


class FlialLocation(models.Model):
    title = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()


class Category(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/', null=True)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Banner(BaseModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banner/')
    description = models.TextField()
    link = models.URLField()
    
    def __str__(self):
        return self.title

class Address(BaseModel):
    longitude = models.FloatField()
    latitude = models.FloatField()
class Brand(BaseModel):  
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='brand')

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    model = models.CharField(max_length=50,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    ram = models.CharField(max_length=20, null =True)
    rom = models.CharField(max_length=20, null =True)
    batary = models.CharField(max_length=30, null =True)
    delivery = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    price_discounted = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Bu yerda yangi maydon qo'shildi

    def __str__(self):
        return self.name
    

class Client(BaseModel):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product", null=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name="address", null=True)
    product_count = models.PositiveIntegerField(default=0, null=True)
    text = models.TextField(null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProductInfoType(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class ProductInfoData(models.Model):
    info_type = models.ForeignKey(ProductInfoType, on_delete=models.CASCADE, related_name='productinfotype')
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')  # Yeni ekleme

    def __str__(self):
        return f"{self.key}: {self.value}"





class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='images', null=True)
    image_1 = models.ImageField(upload_to='products/')
    image_2 = models.ImageField(upload_to='products/')
    image_3 = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"{self.id} - {self.product.name}"


class AboutAshyo(BaseModel):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="Ashyo")
    description = models.TextField()

    def __str__(self):
        return self.title

class Faq(BaseModel):
    question = models.CharField(max_length=255)

class Comment(BaseModel):
    text = models.TextField()  
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='comments')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='comments')
    rate = models.PositiveIntegerField()

    def __str__(self):
        return f"Comment by {self.client} on {self.product}"


class ProductInCart(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField() 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} in cart"



class Order(BaseModel):  
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.client}"