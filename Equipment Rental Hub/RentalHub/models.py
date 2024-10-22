from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    NAME = models.CharField(max_length=50)
    EMAIL = models.EmailField()
    PASSWORD = models.IntegerField()
    DATE_JOINED = models.DateField()

    def __str__(self):
        return self.NAME
class UserProfile(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    DOB = models.DateField()
    ADDRESS = models.TextField()
    PHONE_NO = models.BigIntegerField()

    def __str__(self):
        return self.USER.NAME
class CategoryTable(models.Model):
    Category_NAME = models.CharField(max_length=25)

    def __str__(self):
        return self.Category_NAME
class Equipment(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Equipment_type = models.ForeignKey(CategoryTable, on_delete=models.CASCADE)
    TOOL_NAME = models.CharField(max_length=25)
    DESCRIPTION = models.TextField()
    AVAILABILITY = models.BooleanField(default=False, verbose_name='Active Status')
    Price_Per_Day = models.IntegerField()
    Duration = models.CharField(max_length=25, verbose_name="Enter Duration of Rent")
    Condition = models.CharField(max_length=25)

    def __str__(self):
        return self.TOOL_NAME
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    Total_price = models.IntegerField()
    Booking_from = models.DateField()
    Booking_To = models.DateField()
    Return_Date = models.DateField(null=True)
    Is_Confirmed = models.BooleanField(default=False,verbose_name="Active Status")
    Payment_status = models.BooleanField(default=False)
    PICKUP_LOCATION = models.TextField()
    RETURN_LOCATION = models.TextField()
    DAMAGE_REPORT = models.CharField(max_length=25, null=True)
    LATE_RETURN_PENALTY = models.IntegerField()
    def __str__(self):
        return self.Equipment.TOOL_NAME

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Booking = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    Booking_from = models.DateField()
    Booking_to = models.DateField()
    Payment = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Credit card', 'Credit card'),
        ('Debit card', 'Debit card'),
        ('Digital wallet', 'Digital wallet'),
    ]
    payment_mode = models.CharField(max_length=25, choices=Payment)
    payment_status = models.BooleanField(default=False, verbose_name='Payment Status')
    Payment_date = models.DateField()

    def __str__(self):
        return self.user.NAME
class EquipmentMaintenance(models.Model):
    type = [
        ('Internal', 'Internal'),
        ('External', 'External'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    Maintenance_type = models.CharField( max_length=25, choices=type)
    Maintenance_date = models.DateField()
    cost = models.DecimalField(max_digits=25, decimal_places=2)

    def __str__(self):
        return self.Equipment.TOOL_NAME

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    Rating = models.DecimalField(max_digits=2, decimal_places=2)
    Comment = models.TextField()
    Review_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.NAME
class  Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    Description = models.TextField()
    Date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.NAME
class Contactus(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(verbose_name='Email')
    Subject = models.CharField(max_length=25)
    Message = models.TextField()
    Passport_number = models.IntegerField(null=True)

    def __str__(self):
        return self.Name
