from django.db import models
from django.urls import reverse

# Create your models here.


class Developer(models.Model):
    name_developer = models.CharField(max_length=20)

    def __str__(self):
        return self.name_developer

    def get_absolute_url(self):
        return reverse('detail_dev', args=[str(self.id)])


class Publisher(models.Model):
    name_publisher = models.CharField(max_length=20)
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_publisher

    def get_absolute_url(self):
        return reverse('detail_pub', args=[str(self.id)])


class Tag(models.Model):
    name_tag = models.CharField(max_length=20)


class TypeKey(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    discount = models.IntegerField()
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    typekey_id = models.ForeignKey(TypeKey, on_delete=models.CASCADE)


class Label(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class PaymentDetails(models.Model):
    Owners_name = models.CharField(max_length=30)
    Card = models.IntegerField()
    CVV_code = models.IntegerField()
    CloseDate = models.CharField(max_length=15)


class User(models.Model):
    Nickname = models.CharField(max_length=20)
    Full_name = models.CharField(max_length=40)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=25)
    RegistrationDate = models.DateTimeField(max_length=20)
    paymentdetails_id = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE)


class PaymentHistory(models.Model):
    paysum = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
    payday = models.IntegerField()
    priceback = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class WishList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Basket(models.Model):
    price = models.IntegerField()
    sale = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Statistic(models.Model):
    name = models.CharField(max_length=20)
    amount_product = models.IntegerField()
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)


class Log(models.Model):
    time_out = models.DateTimeField(max_length=15)
    time_entry = models.DateTimeField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Role(models.Model):
    name = models.CharField(max_length=20)
    time_entry = models.DateTimeField(max_length=15)
    dogovor = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



