from django.db import models
from django.contrib.auth.models import User


class Kategoriya(models.Model):
    nomi = models.CharField(max_length=100)
    tavsif = models.TextField()

    def __str__(self):
        return self.nomi


class Mahsulot(models.Model):
    nomi = models.CharField(max_length=200)
    kategoriya = models.ForeignKey(Kategoriya, related_name='mahsulotlar', on_delete=models.CASCADE)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    tavsif = models.TextField()
    rasm = models.ImageField(upload_to='mahsulot_rasmlar/', blank=True, null=True)
    mavjud = models.BooleanField(default=True)  

    def __str__(self):
        return self.nomi


class FoydalanuvchiMalumot(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon_raqami = models.CharField(max_length=20)
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class Buyurtma(models.Model):
    foydalanuvchi = models.ForeignKey(FoydalanuvchiMalumot, on_delete=models.CASCADE)
    jami_summasi = models.DecimalField(max_digits=10, decimal_places=2)
    yetkazib_berish = models.BooleanField(default=True)

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.foydalanuvchi.ism}"


class BuyurtmaItem(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, related_name='itemlar', on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField(default=1)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.mahsulot.nomi} ({self.miqdor} dona)"


class YetkazibBerishManzil(models.Model):
    buyurtma = models.OneToOneField(Buyurtma, on_delete=models.CASCADE)
    viloyat = models.CharField(max_length=100)
    tuman = models.CharField(max_length=100)
    manzil = models.TextField()

    def __str__(self):
        return f"{self.viloyat}, {self.tuman}"


class YagonaSahifa(models.Model):
    mahsulot = models.OneToOneField(Mahsulot, on_delete=models.CASCADE)
    kontent = models.TextField() 
    boshqa_mahsulotlar = models.ManyToManyField(Mahsulot, related_name='boshqa_mahsulotlar', blank=True) 

    def __str__(self):
        return f"{self.mahsulot.nomi} sahifasi"
