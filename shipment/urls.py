from django.urls import path
from shipment.views import ShipmentCreateAPIView, ShipmentDetailView

urlpatterns = [
    path('shipment', ShipmentCreateAPIView.as_view(), name='shipment'),
    path('shipment-detail', ShipmentDetailView.as_view(), name='shipment-detail')
]
