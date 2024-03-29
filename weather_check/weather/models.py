from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name_plural = "Cities"
    
    def __str__(self):
        return self.name