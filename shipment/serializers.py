from rest_framework import serializers
from .models import Shipment, Address, Parcel

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
    
class ParcelSerializer(serializers.ModelSerializer):
    length = serializers.IntegerField(required=True)
    width = serializers.IntegerField(required=True)
    height = serializers.IntegerField(required=True)

    class Meta:
        model = Parcel
        fields = ['length', 'width', 'height', 'weight']
    def to_representation(self, instance):
        return {
            'length': instance.length,
            'width': instance.width,
            'height': instance.height,
            'weight': instance.weight,
        }
    def create(self, validated_data):
        return Parcel.objects.create(**validated_data)

class ShipmentSerializer(serializers.ModelSerializer):
    to_address = AddressSerializer()
    from_address = AddressSerializer()
    parcel = ParcelSerializer()

    class Meta:
        model = Shipment
        fields = '__all__'

    def create(self, validated_data):
        
        to_address_data = validated_data.pop('to_address')
        from_address_data = validated_data.pop('from_address')
        parcel_data = validated_data.pop('parcel')

        to_address_serializer = AddressSerializer(data=to_address_data)
        to_address_serializer.is_valid(raise_exception=True)
        to_address = to_address_serializer.save()

        from_address_serializer = AddressSerializer(data=from_address_data)
        from_address_serializer.is_valid(raise_exception=True)
        from_address = from_address_serializer.save()

        parcel_serializer = ParcelSerializer(data=parcel_data)
        parcel_serializer.is_valid(raise_exception=True)
        parcel = parcel_serializer.save()

        shipment = Shipment.objects.create(to_address=to_address, from_address=from_address, parcel=parcel, **validated_data)

        return shipment