from django.db import models
from django.utils import timezone

class Product(models.Model):
    nom = models.CharField(max_length=250)
    prix = models.FloatField(max_length=250)

    def __init__(self, n, p): 
        self.nom = n
        self.prix = p
   
