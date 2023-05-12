from django.conf import settings
api_key = settings.EASYPOST_API_KEY
import urllib.request
import json
from urllib import request, error
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ShipmentSerializer


class ShipmentCreateAPIView(APIView):
    def post(self, request, format=None):
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            # breakpoint()
            url = 'https://api.easypost.com/v2/shipments'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {settings.EASYPOST_API_KEY}',
            }
            data = serializer.validated_data
            payload = {
                'shipment': {
                    'to_address': {
                        'name': data['to_address']['name'],
                        'street1': data['to_address']['street1'],
                        'street2': data['to_address']['street2'],
                        'city': data['to_address']['city'],
                        'state': data['to_address']['state'],
                        'zip_code': data['to_address']['zip_code'],
                        'country': data['to_address']['country']
                    },
                    'from_address': {
                        'name': data['from_address']['name'],
                        'street1': data['from_address']['street1'],
                        'street2': data['from_address']['street2'],
                        'city': data['from_address']['city'],
                        'state': data['from_address']['state'],
                        'zip_code': data['from_address']['zip_code'],
                        'country': data['from_address']['country']
                    },
                    'parcel': {
                        'weight': float(data['parcel']['weight']),
                        'length': float(data['parcel']['length']),
                        'width': float(data['parcel']['width']),
                        'height': float(data['parcel']['height'])
                    }
                }
            }
            try:
                
                req = urllib.request.Request(url, headers=headers, method='POST', data=json.dumps(payload).encode('utf-8'))
                with urllib.request.urlopen(req) as response:
                    if response.status == 200:
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(json.loads(response.read().decode('utf-8')), status=response.status)
            except error.HTTPError as e:
                return Response(json.loads(e.read().decode('utf-8')), status=e.code)
            except error.URLError as e:
                return Response(str(e.reason), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShipmentDetailView(APIView):
    def get(self, request, format=None):
        shipment_id = request.data['shipment_id']
        url = f'https://api.easypost.com/v2/shipments/{shipment_id}'     
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {settings.EASYPOST_API_KEY}',
        }
        breakpoint()
        response = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read().decode()
        shipment_data = json.loads(response)
        return Response(shipment_data)