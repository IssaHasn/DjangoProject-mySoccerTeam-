from django.db import models

class Players(models.Model):
    
    name = models.CharField( max_length = 20, null = True)
    lastName = models.CharField(max_length = 20)
    age = models.IntegerField(blank = True)
    phoneNumber = models.IntegerField(blank = True)

    def __str__(self):
        return f"{self.name} {self.lastName}"

    class Meta:
        verbose_name = 'Player'