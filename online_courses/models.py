from django.db import models
from PIL import Image

# Create your models here.



class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.save(self.image.path)



class new_des(models.Model):
    name = models.CharField(max_length = 100)
    add = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)