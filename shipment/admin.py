from django.contrib import admin
from shipment.models import Address, Parcel, Shipment


admin.site.register(Address)
admin.site.register(Parcel)
admin.site.register(Shipment)

