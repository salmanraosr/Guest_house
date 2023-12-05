from django.contrib import admin

# Register your models here.
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from.models import GuestHouses
from.models import RoomCategories
from.models import GuestCategories
from.models import RoomRates,Approval,Rooms,Reservation

# Create your models here.
from .models import User, Customer, Employee,Request

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Request)
admin.site.register(Approval)

admin.site.register(Reservation)
@admin.register(GuestHouses)
class GuestHousesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(RoomCategories)
class RoomCategoriesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','guesthouse_name', 'room_cat' ]

@admin.register(GuestCategories)
class GuestCategoriesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','room_category' ,'guestcategory_name']

@admin.register(RoomRates)
class RoomRatesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','room_category_id','guest_category','rate']


@admin.register(Rooms)
class RoomsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','GuestHouses','RoomCategories','is_available','room_no','room_desc','room_capacity']
