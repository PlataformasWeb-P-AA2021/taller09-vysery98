from django.db import models

# Create your models here.

class Parroquia(models.Model):
    
    class Meta:
        verbose_name_plural = "Parroquias"
    
    opciones_tipo_parroquia = (
            ('urbana', 'Urbana'),
            ('rural', 'Rural'),
        )

    nombre = models.CharField("Nombre de Parroquia:", max_length=50)
    tipo_parroquia = models.CharField("Tipo de Parroquia", max_length=10, \
            choices=opciones_tipo_parroquia) 

    def __str__(self):
        return "%s - %s" % (self.nombre,
                self.tipo_parroquia)


class Barrio(models.Model):
    
    opciones_num_parques = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
        )

    nombre = models.CharField("Nombre de Barrio o Ciudadela:", max_length=50)
    num_viviendas = models.CharField("Número de viviendas:", max_length=10)
    num_parques = models.CharField("Número de parques", \
        choices=opciones_num_parques, max_length=10)
    num_edificios = models.CharField("Número de edificios", max_length=30)
    parroquia = models.ForeignKey(Parroquia, related_name='lasparroquias', 
        on_delete = models.CASCADE)

    def __str__(self):
        return "Barrio o Ciudadela: %s - %s - %s - %s - %s" % (
                        self.nombre,
                        self.num_viviendas,
                        self.num_parques,
                        self.num_edificios,
                        self.parroquia)
