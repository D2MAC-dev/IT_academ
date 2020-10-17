from django.db import models

# Create your models here.

class PhoneType(models.Model):
    phone_type = models.CharField(
        'Тип телефонного номера',
        max_length=5
    )

description = models.TextField(
    'Описание', 
    blank=True
    null=True
)

def __str__(self):
    return self.phone_type




# class Phone(models.Model):  #принято называть в ед.числе
#     # id/pk = autoinc pk  
#      number = models.CharField(
#          'Номер телефона',
#          max_length="20",
#          blank=False,
#          null=False    
     )