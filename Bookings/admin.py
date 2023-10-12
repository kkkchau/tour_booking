from django.contrib import admin
from Bookings.models import Status,Tour,Customer,Booking,Search
# Register your models here.

class CustTour(admin.ModelAdmin):
	list_display=('name', 'description', 'location','visitorCount','cost')
	list_filter=('name','cost')
admin.site.register(Tour, CustTour)


class CustCustomer(admin.ModelAdmin):
	list_display=('name','contact','email','address')
	list_filter=('name','contact')
admin.site.register(Customer, CustCustomer)

admin.site.register(Status)


class CustBooking(admin.ModelAdmin):
	list_display=('h_id','c_id','time','amount','status')
	list_filter=('h_id','status')
admin.site.register(Booking, CustBooking)


