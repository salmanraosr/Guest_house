from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Employee,Request,RoomRates,GuestCategories,Approval,GuestHouses,RoomCategories,Rooms,Reservation
from django import forms


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.save()
        return user


class EmployeeSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.save()
        employee = Employee.objects.create(user=user)
        employee.save()
        return user


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = "__all__"

        widgets = {
            'checkin': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'checkout': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            )
        }

class RateForm(forms.ModelForm):
    class Meta:
        model = RoomRates
        fields = "__all__"
class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Approval
        fields = "__all__"

class GuesthouseForm(forms.ModelForm):
    class Meta:
        model = GuestHouses
        fields = "__all__"

class RoomCategoriesForm(forms.ModelForm):
    class Meta:
        model = RoomCategories
        fields = "__all__"
class GuestCategoriesForm(forms.ModelForm):
    class Meta:
        model = GuestCategories
        fields = "__all__"
class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = "__all__"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['GuestHouses', 'RoomCategories', 'guest_category', 'rooms', 'room_rate', 'employee', 'customer', 'checkin', 'checkout', 'no_of_days', 'total_amount']
        widgets = {
            'checkin': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}),
            'checkout': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'first_name','last_name','address','country','state','city','mobile_no','aadhar_no']
class RoomRateForm(forms.ModelForm):
    class Meta:
        model = RoomRates
        fields = ['room_category_id', 'guest_category', 'rate']
