
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return (self.username)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, unique=False,null=True)
    last_name = models.CharField(max_length=100, unique=False, null=True)
    address = models.CharField(max_length=100, unique=False, null=True)
    country = models.CharField(max_length=100, unique=False, null=True)
    state = models.CharField(max_length=100, unique=False, null=True)
    city = models.CharField(max_length=100, unique=False, null=True)
    mobile_no = models.CharField(max_length=100, unique=False, null=True)
    aadhar_no = models.CharField(max_length=100, unique=False, null=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class GuestHouses(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RoomCategories(models.Model):
    guesthouse_name = models.ForeignKey(GuestHouses, on_delete=models.CASCADE)
    room_cat = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.room_cat


class GuestCategories(models.Model):
    room_category = models.ForeignKey(RoomCategories, on_delete=models.CASCADE)
    guestcategory_name = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.guestcategory_name

class RoomRates(models.Model):
    room_category_id = models.ForeignKey(RoomCategories, on_delete=models.CASCADE)
    guest_category = models.ForeignKey(GuestCategories, on_delete=models.CASCADE)
    rate = models.FloatField(null=True)

    def __str__(self):
        return str(self.rate)


class Request(models.Model):
    name = models.CharField(max_length=100, unique=False)
    email = models.EmailField(max_length=100)
    mob = models.IntegerField(null=True)
    id_proof_no = models.IntegerField(null=True)
    no_of_persons = models.IntegerField(null=True)
    no_of_rooms = models.IntegerField(null=True)
    checkin = models.DateField(blank=True, null=True)
    checkout = models.DateField(blank=True, null=True)
    request_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "request"


class Approval(models.Model):
    request= models.ForeignKey(Request, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    approval_date=models.DateTimeField(auto_now=True)
    approved_by=models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.approved_by)

    class Meta:
        db_table = "approval"

class Rooms(models.Model):
    GuestHouses=models.ForeignKey(GuestHouses, on_delete=models.CASCADE)
    RoomCategories=models.ForeignKey(RoomCategories, on_delete=models.CASCADE)
    is_available=models.BooleanField(default=False)
    room_no=models.CharField(max_length=100, unique=False)
    room_desc=models.CharField(max_length=100, unique=False)
    room_capacity=models.IntegerField()

    def __str__(self):
        return self.room_no
    class Meta:
        db_table = "rooms"

class Reservation(models.Model):
    GuestHouses = models.ForeignKey(GuestHouses, on_delete=models.CASCADE)
    RoomCategories = models.ForeignKey(RoomCategories, on_delete=models.CASCADE)
    guest_category = models.ForeignKey(GuestCategories, on_delete=models.CASCADE, null=True)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room_rate = models.ForeignKey(RoomRates, on_delete=models.CASCADE)
    checkin = models.DateField(blank=True, null=True)
    checkout = models.DateField(blank=True, null=True)
    no_of_days = models.IntegerField()
    total_amount = models.FloatField()

    class Meta:
        db_table = "reservation"





