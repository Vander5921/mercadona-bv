from django.db import models

class Article(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='articles_images/')
    promotion = models.ForeignKey('promotion.Promotion', on_delete=models.SET_NULL, null=True, blank=True)