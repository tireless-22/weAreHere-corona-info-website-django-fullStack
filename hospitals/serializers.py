from rest_framework import serializers
from .models import *


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State 
        fields = ['state']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District 
        fields = ['state','district']

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name_of_hospital','district','address','gmap_link','pincode','total_icu_beds','total_icu_ventilator_beds','total_o2_beds','total_normal_beds','contact_number_of_the_hospital']

class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulances
        fields = ['district','vehicle_no_of_the_ambulance','name_of_the_ambulance_driver','contact_no_of_ambulance_driver','address','gmap_link','pincode']

class OxygenSerializer(serializers.ModelSerializer):
    class Meta:
        model = oxygen_cylinders
        fields = ['district','name_of_the_oxygen_dealer','contact_no_of_the_oxygen_dealer','address','gmap_link','pincode']

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = ['district','name_of_the_medical_store','name_of_the_shop_owner','contact_no_of_the_medical_shop_owner','address','gmap_link','pincode']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History  
        fields = ['hospital','last_updated','icu_beds','o2_beds','normal_beds']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffData
        fields = ['hospital','ambulance','oxygen','designation','contact']
