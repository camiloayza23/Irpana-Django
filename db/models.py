from django.db import models

# Create your models here.


class Highlights(models.Model):
    id_highlight   = models.AutoField(primary_key=True, unique=True)
    titulo         = models.CharField(max_length=100)
    descripcion    = models.TextField()
    precio         = models.DecimalField(max_digits=5,decimal_places=3, blank=True, default=None, null=True)
    fotos          = models.FileField(upload_to='documents/', null=True, blank=True)
    
    def __str__(self):
        return 'Highlight: ' + self.titulo
class Tipos(models.Model):
    id_tipos    = models.AutoField(primary_key=True, unique=True)
    tipo        = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return 'Tipo: ' + self.tipo

class Zonas(models.Model):
    id_zonas    = models.AutoField(primary_key=True, unique=True)
    zona        = models.CharField(max_length=100)

    def __str__(self):
        return 'Zona: ' + self.zona

class Lugar(models.Model):
    id_lugar    = models.AutoField(primary_key=True, unique=True)
    nombre      = models.CharField(max_length=100)
    zona        = models.ForeignKey(Zonas,on_delete=models.CASCADE)
    direccion   = models.CharField(max_length=100)
    tel         = models.IntegerField()
    highlight   = models.ForeignKey(Highlights,on_delete=models.CASCADE)
    email       = models.EmailField()
    fb          = models.CharField(max_length=100)
    insta       = models.CharField(max_length=100)
    tipo        = models.ForeignKey(Tipos,on_delete=models.CASCADE)
    horario     = models.CharField(max_length=100)

    def __str__(self):
        return 'Lugar: ' + self.nombre
