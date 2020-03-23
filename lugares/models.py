from django.db import models

# Create your models here.

class Lugar(models.Model):
    nombre      = models.TextField()
    zona        = models.TextField()
    direccion   = models.TextField()
    email        = models.EmailField()
    fb   = models.TextField()
    insta         = models.TextField()
    tipo  = models.TextField()
    horario = models.TextField()

