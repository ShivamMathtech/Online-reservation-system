from django.db import models

class User_info(models.Model):
    faname= models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)
    state =models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    gender=models.IntegerField()

    class Meta:
        db_table='user_info'

class flight_search(models.Model):
    source=models.CharField(max_length=100)
    destinition=models.CharField(max_length=100)
    date =models.DateField()
    
    class Meta:
        db_table='flights'

class Booking(models.Model):
    user_id=models.IntegerField();
    route_id=models.IntegerField()
    class_type=models.CharField(max_length=50)
    date=models.DateField()

    class Meta:
        db_table='booking'
class payment(models.Model):
    user_id=models.IntegerField()
    amount=models.IntegerField()        
    date=models.DateField()

    class Meta:
        db_table='payment'