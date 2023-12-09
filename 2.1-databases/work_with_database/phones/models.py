from django.db import models



class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,null=False)
    image = models.URLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(max_length=50)
