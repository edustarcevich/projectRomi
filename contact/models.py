from django.db import models

# Create your models here.

class Enviar_Email_to (models.Model):
    asunto = models.CharField (max_length=50)
    email = models.EmailField (max_length=200)
    mensaje = models.TextField ()
