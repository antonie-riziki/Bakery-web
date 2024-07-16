from django.db import models


# Create your models here.
class Portfolio(models.Model):
    project_name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    portfolio_image = models.FileField(upload_to='img')

    def __str__(self):
        return self.project_name


class Testimonial(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    customer_testimony = models.CharField(max_length=200, null=True)
    customer_image = models.FileField(upload_to='img')

    def __str__(self):
        return self.customer_name


class Blog(models.Model):
    blog_header = models.CharField(max_length=200, null=True)
    date_posted = models.DateField()
    blog_content = models.CharField(max_length=1000, null=True)
    blog_image = models.FileField(upload_to='img')

    def __str__(self):
        return self.blog_header


class Product(models.Model):
    prod_name = models.CharField(max_length=200, null=True)
    prod_category = models.CharField(max_length=200, null=True)
    prod_img = models.FileField(upload_to='img')
    prod_price = models.IntegerField(null=True)

    def __str__(self):
        return self.prod_name


class GraduationCake(models.Model):
    description = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to='img')
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.description


class ThemedCake(models.Model):
    description = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to='img')
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.description


class BirthdayCake(models.Model):
    description = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to='img')
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.description


class BabyShowerCake(models.Model):
    description = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to='img')
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.description


class WeddingCake(models.Model):
    description = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to='img')
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.description


class CupCake(models.Model):
    description = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to='img')
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.description