from django.contrib import admin
from .models import (Client, Category, ProductInfoData,
                     ProductInfoType, Product, Brand,  
                     ProductImages, Banner, Address, FlialLocation, 
                     AboutAshyo, Faq, Comment, ProductInCart, 
                     Order,Kredit,
                     PymentType)


admin.site.register(Client)
admin.site.register(PymentType)
admin.site.register(Kredit)

admin.site.register(Category)
admin.site.register(ProductInfoData)
admin.site.register(ProductInfoType)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ProductImages)
admin.site.register(AboutAshyo)
admin.site.register(Comment)
admin.site.register(ProductInCart)
admin.site.register(Banner)
admin.site.register(Order)
admin.site.register(FlialLocation)
admin.site.register(Address)
admin.site.register(Faq)

