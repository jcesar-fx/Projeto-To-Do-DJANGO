from django.db import models # type: ignore
from django.contrib.auth import get_user_model # type: ignore
# Create your models here.

class Task(models.Model):
    STATUS = ('doing', 'doing'), ('done', 'done')
    tittle = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5,   
                            choices=STATUS,)
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    