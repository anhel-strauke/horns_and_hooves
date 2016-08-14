from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField()
    #small_image = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
    #        ResizeToFill(50, 50)], image_field='image',
    #        format='JPEG', options={'quality': 90})
    description = models.TextField(max_length = 1000)
    category = models.ForeignKey(Category)
    price = models.FloatField()

    def __str__(self):
        return self.name
    


# Create your models here.
