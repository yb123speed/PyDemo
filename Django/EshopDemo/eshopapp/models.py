from django.db import models

# Create your models here.

class Product(models.Model):
    # 如同其他的ORM，ID字段是默认声明的，不需要单独处理.
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image_url = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)

