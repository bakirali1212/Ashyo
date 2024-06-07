from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from phonenumber_field.modelfields import PhoneNumberField




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
    price_discounted = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 

    def __str__(self):
        return self.name
    
class Region(BaseModel):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Tuman(BaseModel):
    name = models.CharField(max_length=100, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='region1',null=True)

    def __str__(self):
        return self.name

class ShippingAddress(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='region2',null=True)
    tuman = models.ForeignKey(Tuman, on_delete=models.PROTECT, related_name='tuman', null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.address



class Client(BaseModel):
    class PymentChoice(models.TextChoices):
        CART = "cart","Cart"
        NAQD = "naqd","Naqd"
        CREDIT = "credit","Credit"
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product", null=True)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.PROTECT, related_name="shipping_adsress", null=True)
    product_count = models.PositiveIntegerField(default=0, null=True)
    text = models.TextField(null=True)
    pyment = models.CharField(max_length=55, choices=PymentChoice.choices, default=PymentChoice.NAQD)
    # pyment = models.ForeignKey(PymentType, on_delete=models.PROTECT, related_name="pyment", null=True)


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


    

    def __str__(self):
        return f"Order {self.id} by {self.client}"
    

class PhoneManager(BaseUserManager):
    use_in_migrations = True

    def normalize_phone(self, phone):
     
        return phone.strip()

    def _create_user(self, phone, email, password=None, **extra_fields):
        
        if not phone:
            raise ValueError("Telefon raqami kiritilishi shart")
        email = self.normalize_email(email)
        phone = self.normalize_phone(phone)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser bo'lishi uchun is_staff=True bo'lishi kerak.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser bo'lishi uchun is_superuser=True bo'lishi kerak.")

        return self._create_user(phone, email, password, **extra_fields)



class User(AbstractUser):
    class UserAuthStatus(models.TextChoices):
        NEW = 'new', 'Yangi'
        APPROVED = 'approved', 'Tasdiqlangan'

    phone = PhoneNumberField(unique= True)
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = PhoneManager()
    # app_user.username
    status = models.CharField(max_length=50,choices=UserAuthStatus.choices, default='new')

    code = models.CharField(max_length=4,null=True)
    expire_date = models.DateTimeField(null=True)


    def __str__(self) -> str:
        return f"{self.id}-{self.phone}"