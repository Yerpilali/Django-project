from django.contrib import admin
from .models import (Developer,
                     Publisher,
                     Tag,
                     TypeKey,
                     Product,
                     Label,
                     PaymentDetails,
                     User,
                     PaymentHistory,
                     WishList,
                     Basket,
                     Statistic,
                     Log,
                     Role)
# Register your models here.

admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Tag)
admin.site.register(TypeKey)
admin.site.register(Product)
admin.site.register(Label)
admin.site.register(PaymentDetails)
admin.site.register(User)
admin.site.register(PaymentHistory)
admin.site.register(WishList)
admin.site.register(Basket)
admin.site.register(Statistic)
admin.site.register(Log)
admin.site.register(Role)
