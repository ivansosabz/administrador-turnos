from django.db import models
from usuarios.models import Grupo

# Create your models here.

class Responsable (models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#000000')
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Ciclo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    intervalo_dias = models.IntegerField()
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CicloOrden(models.Model):
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    posicion = models.IntegerField()

class TurnoReal(models.Model):
    TIPO_CHOICES = [
        ("normal", "Normal"),  # Durmió quien le tocaba
        ("cobertura", "Cobertura"),  # Otra persona cubrió esta noche
        ("intercambio", "Intercambio"),  # Cambio de turno acordado
    ]
    responsable_original = models.ForeignKey(
        Responsable,
        on_delete=models.CASCADE,
        related_name="responsable_original",
    )
    responsable_reemplazo = models.ForeignKey(
        Responsable,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="responsable_reemplazo",
    )
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipoTurno = models.CharField(max_length=20, choices=TIPO_CHOICES, default="normal")
    notas = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tipoTurno
