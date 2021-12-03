from django.db import models


# Create your models here.
class User(models.Model):                   #need to change class name
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    mail_add = models.CharField(max_length=200, null=True)
    bill_add = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.name

# class Ticket(models.Model):
#     ticket_number= models.IntegerField(null=True)
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.ForeignKey(User, on_delete=models.CASCADE)
#     guestcount = models.IntegerField()
#     reservation_date = models.DateTimeField(auto_now_add=True, null=True)
#     reservation_time = models.TimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.ticket_number



class Tables(models.Model):
    TABLE_CAPACITY=(
        ('2', 'T2'),
        ('3', 'T3'),
        ('4', 'T4'),
        ('5', 'T5'),
        ('6', 'T6'),
        ('7', 'T7'),
        ('8', 'T8'),
        ('9', 'T9'),
        ('10', 'T10'),
    )

    isAvailable=models.BooleanField(null=True)
    table_number = models.IntegerField()
    category = models.CharField(max_length=2, choices=TABLE_CAPACITY)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table #{self.table_number}: capicity of {self.capacity} seats. Availability:{self.isAvailable}"

class UserReservation(models.Model):
    name= models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    number_guest=models.IntegerField(null=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)

    def __str__(self):
        return f"{self.name} reserved a table"
