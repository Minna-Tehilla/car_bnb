from rest_framework import serializers
from .models import *


class MessageSerializer (serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"


class CarSerializer (serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class PersonSerializer (serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class RentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = "__all__"

# class BikeSerializer( serializers.ModelSerializer):


# find out about the personserilazier that should give me a
# car_sr=et with many=true, do i need to put all sadot in it?)
# how exactly does it work??


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'
        depth = 0

    def save(self):
        new_factory = Factory(
            name=self.validated_data['name'],
            address=self.validated_data['address'],
        )
        new_factory.save()
        return new_factory


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'
        depth = 1

    def save(self, **kwargs):
        new_bike = Bike(
            plate_number=self.validated_data['plate_number'],
            km=self.validated_data['km'],
            year=self.validated_data['year'],
            # volume=self.validated_data['volume'],
            factory=self.instance
        )
        new_bike.save()
        return new_bike
