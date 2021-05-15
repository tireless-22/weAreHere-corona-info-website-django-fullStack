from django.core.validators import MinValueValidator, MaxLengthValidator, MinLengthValidator
from django.db import models
from django.db.models.deletion import CASCADE


class State(models.Model):
	state = models.CharField(max_length=50,null=False)

class District(models.Model):
	state = models.ForeignKey(State,on_delete=CASCADE)
	district = models.CharField(max_length=50,null=False)

class Hospital(models.Model):
    name_of_hospital = models.CharField(max_length=50, null=False)
    district = models.ForeignKey(District,on_delete=CASCADE, related_name='dist')
    address = models.CharField(max_length=100, null=False)
    gmap_link = models.CharField(max_length=2048, null=False)
    pincode = models.IntegerField(null=False)
    total_icu_beds = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    total_icu_ventilator_beds=models.IntegerField(default=0, validators=[MinValueValidator(0)])
    total_o2_beds = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    total_normal_beds = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    contact_number_of_the_hospital= models.BigIntegerField(default=0, validators=[MinValueValidator(0)])


class Ambulances(models.Model):
    district = models.ForeignKey(District,on_delete=CASCADE)
    vehicle_no_of_the_ambulance = models.CharField(max_length=30,null=False)
    name_of_the_ambulance_driver = models.CharField(max_length=30,null=False)
    contact_no_of_ambulance_driver=models.IntegerField(default=0, validators=[MinValueValidator(0)])

class oxygen_cylinders(models.Model):
    district = models.ForeignKey(District,on_delete=CASCADE)
    name_of_the_oxygen_dealer= models.CharField(max_length=30,null=False)
    contact_no_of_the_oxygen_dealer=models.IntegerField(default=0, validators=[MinValueValidator(0)])

class Medicines(models.Model):
    district = models.ForeignKey(District,on_delete=CASCADE)
    name_of_the_medical_store= models.CharField(max_length=30,null=False)
    name_of_the_shop_owner= models.CharField(max_length=30,null=False)
    contact_no_of_the_medical_shop_owner=models.IntegerField(default=0, validators=[MinValueValidator(0)])

class History(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    last_updated = models.DateTimeField()
    icu_beds = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    o2_beds = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    normal_beds = models.IntegerField(null=False, validators=[MinValueValidator(0)])


class StaffData(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    ambulance = models.ForeignKey(Ambulances, on_delete=models.CASCADE)
    oxygen = models.ForeignKey(oxygen_cylinders, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=False)
    contact = models.IntegerField(validators=[MaxLengthValidator(10), MinLengthValidator(10)], null=False)