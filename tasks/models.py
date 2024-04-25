from django.db import models # type: ignore

# Create your models here.
class Task(models.Model):
    STATUS = ('doing', 'Doing'), ('done', 'Done')
    tittle = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5,   
                            choices=STATUS,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)