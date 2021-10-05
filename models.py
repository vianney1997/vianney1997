from django.db import models
from django.urls import reverse
import uuid


#First model
class CarType(models.Model):
    #heredoc
    """ Model that represents the car type """
    car_type = models.CharField(max_length = 200, help_text = 'Please enter car type (e.g. SUV, Saloon...)')

    def __str__(self):
        return self.car_type

#Second model
class CarMake(models.Model):
    """Model that represent a car make"""
    #'Make' is a verbose_name
    car_make = models.CharField('Make', max_length = 200, help_text = 'Please enter car make (e.g. Toyota, Nissan...)')

    def __str__(self):
        return self.car_make

#Third model
class CarModel(models.Model):
    """Model that represents car model"""

    car_model = models.CharField('Model', max_length = 200, help_text = 'Please enter car model (e.g. Corolla, Sunny...)')
    car_image = models.ImageField('car_image', upload_to='images/', null = True)

    def __str__(self):
        return self.car_model

#Forth model
class Car(models.Model):
    """Model that represents a car"""
    registration = models.CharField('Reg No.', max_length = 7, unique = True)
    car_type = models.ForeignKey(CarType, on_delete = models.RESTRICT)
    car_make = models.ForeignKey(CarMake, on_delete = models.RESTRICT)
    car_model = models.ForeignKey(CarModel, on_delete = models.RESTRICT)
    description = models.TextField(max_length = 1000, help_text = "Some additional info about the car")
    car_image = models.ImageField('car_image', upload_to='images/', null = True)

    def __str__(self):
        return  (f'{self.car_make} {self.car_model} {self.registration}')

#Fifth model
class CarOwner(models.Model):
    """Model that represents a car owners"""
    owner_name = models.CharField('owner_name', max_length = 200, help_text = 'Please enter your full name (e.g. David, Kamau...)')
    owner_IDno = models.CharField('owner_IDno', max_length = 8, unique = True, help_text = 'Please enter your ID number (e.g. 12345678...)')
    owner_email = models.CharField('owner_email', max_length = 200, help_text = 'Please enter your email (e.g. david@gmail.com)')
    car = models.ForeignKey('Car', on_delete = models.RESTRICT, null = True)
    car_image = models.ImageField('car_image', upload_to='images/', null = True)

    def __str__(self):
        return  (f'{self.owner_name} {self.owner_email} {self.car}')


    #reverse the object to generate a URL to the string output
    def get_absolute_url (self):
        # returns a URL to generate a detailed car record
        return reverse('car-detail', args=[str(self.id)])

class carInstance(models.Model):
    """Model to represent a car instance"""

    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    car = models.ForeignKey('Car', on_delete = models.RESTRICT, null = True)
    imprint = models.CharField(max_length = 500)
    due_back = models.DateField(null = True, blank = True) 

    hire_status = (
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
        ('m', 'Maintenance'),
    )

    status = models.CharField(
        max_length = 1,
        choices = hire_status,
        blank = True,
        default = 'a',
        help_text = 'Car Availability'  
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} {self.car}'
