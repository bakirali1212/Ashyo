from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Client(BaseModel):
    class ClientPayChoices(models.TextChoices):
        NAQD = "naqd", "Naqd"
        KREDIT = "kredit", "Kredit"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    pay = models.CharField(max_length=55, choices=ClientPayChoices.choices, default=ClientPayChoices.NAQD)
    passport_img = models.ImageField(upload_to="passport")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icon')

    def __str__(self):
        return self.name


class Characteristics(BaseModel):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)  
    size = models.CharField(max_length=50, null=True, blank=True)
    accumulator = models.CharField(max_length=50, null=True, blank=True)
    ram = models.CharField(max_length=50, null=True, blank=True)
    rom = models.CharField(max_length=50, null=True, blank=True)
    processor = models.CharField(max_length=50, null=True, blank=True)
    simcard = models.CharField(max_length=50, null=True, blank=True)
    core = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.model


class Product(BaseModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    img = models.ImageField(upload_to="images")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    characteristics = models.ForeignKey(Characteristics, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.name


class Brand(BaseModel):  
    name = models.CharField(max_length=50)
    add_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='brands')
    img = models.ImageField(upload_to='brand')

    def __str__(self):
        return self.name


class ProductMemory(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='memories')
    add_price = models.DecimalField(max_digits=10, decimal_places=2)
    memory = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.memory} - {self.product.name}"


class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='images')
    color = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='products/')
    image_2 = models.ImageField(upload_to='products/')
    image_3 = models.ImageField(upload_to='products/')
    add_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.color} - {self.product.name}"


class AboutAshyo(BaseModel):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="Ashyo")
    description = models.TextField()

    def __str__(self):
        return self.title


class Comment(BaseModel):
    text = models.TextField()  
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='comments')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='comments')
    rate = models.PositiveIntegerField()

    def __str__(self):
        return f"Comment by {self.client} on {self.product}"


class ProductInCart(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    product_color = models.ForeignKey(ProductImages, on_delete=models.CASCADE, related_name='cart_items')
    product_size = models.ForeignKey(ProductMemory, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='cart_items')  
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} in cart"


class Order(BaseModel):  
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.client}"
