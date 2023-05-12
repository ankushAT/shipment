from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=255)
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class Parcel(models.Model):
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

# class CustomsInfo(models.Model):
#     id = models.CharField(max_length=255)
#     # Add any other relevant customs information here

class Shipment(models.Model):
    to_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='shipments_to')
    from_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='shipments_from')
    parcel = models.OneToOneField(Parcel, on_delete=models.CASCADE, related_name='shipment')
