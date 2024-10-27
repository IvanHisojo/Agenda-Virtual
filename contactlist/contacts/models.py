from django.db import models
import imagekit


# Create your models here.
class Contact(models.Model):
    avatar= models.ImageField(upload_to='contact',null=True,blank=True)
    name = models.CharField(max_length=100,verbose_name='Nombre')
    email = models.EmailField(max_length=50,verbose_name='Correo')
    birth = models.DateField(null=True,blank=True,verbose_name='Cumpleaños')
    phone = models.CharField(max_length=15,null=True,blank=True,verbose_name='Número telefónico')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

#correr servidor
#docker run -d -p 8000:8000 --name mi_django_container nombre-de-tu-imagen

#eliminar contenedor
#docker rm -f mi_django_container

