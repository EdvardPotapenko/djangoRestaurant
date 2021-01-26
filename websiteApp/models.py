from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} : {self.category_order}'