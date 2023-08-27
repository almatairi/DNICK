from django.db import models

class Cake(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='cakeimages/')
    price = models.IntegerField(default=0)
    # occasion = models.CharField(choices=OCCASION , max_length=255)
    # servingSize = models.CharField(choices=SERVING_SIZE , max_length=255)
    # flavor = models.CharField(choices=FLAVORS , max_length=255)
    # toppings = models.CharField(choices=TOPPINGS , max_length=255)
    # cardMessage = models.CharField(max_length=255)

    def __str__(self):
        return str(f'{self.name} - {self.price}')
    
    def get_url(self):
        if self.url:
            return self.url
        else:
            return f'/cakeimages/{self.id}/image'
        
class OrderedCakes(models.Model):
    cake = models.OneToOneField(Cake, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='Ordered-cakeimages/')
    price = models.IntegerField(default=0)
    occasion = models.CharField(max_length=255)
    servingSize = models.CharField(max_length=255)
    flavor = models.CharField(max_length=255)
    toppings = models.CharField(max_length=255)
    cardMessage = models.CharField(max_length=255)

    def __str__(self):
        return str(f'{self.name} - {self.price}')
