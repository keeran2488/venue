from django.contrib import admin

from .models import VenueDetails, Customer


admin.site.register(Customer)
admin.site.register(VenueDetails)
