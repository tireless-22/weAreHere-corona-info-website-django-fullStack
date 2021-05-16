from django.shortcuts import render
from django.http import HttpResponse 
from django.db.models.query import QuerySet
from .models import *
from rest_framework import viewsets
from .serializers import *


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class AmbulanceViewSet(viewsets.ModelViewSet):
    queryset = Ambulances.objects.all()
    serializer_class = AmbulanceSerializer

class OxygenViewSet(viewsets.ModelViewSet):
    queryset = oxygen_cylinders.objects.all()
    serializer_class = OxygenSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicines.objects.all()
    serializer_class = MedicineSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = StaffData.objects.all()
    serializer_class = StaffSerializer



def index(request):
	states = State.objects.all()
	w = {}
	for i in states:
		# print(i.state)
		w[i.state] = []
		dist = District.objects.filter(state_id=i)
		#print(dist.district)
		for j in dist:
			w[i.state].append(j.district)
	# print(w)
	return render(request,'index.html',{'w':w})


def results(request):
    pass



def services(request,id1,id2):
	states = State.objects.filter(state=id1)
	# print(type(states))
	# here states is an object
	# we can not use them directly it is will print like <QuerySet [<State: State object (1)>]>
	# and this object object is of type class like <class 'django.db.models.query.QuerySet'>
	# y beacause we are filtering  this from the model class 

	# print(states[0])
	dist = District.objects.filter(district=id2)
	#print(dist[0].district)


	lst = []
	lst.append(states[0].state)
	lst.append(dist[0].district)
	print(lst)



	hosp = Hospital.objects.filter(district_id=dist[0])
	ambu = Ambulances.objects.filter(district_id=dist[0])
	oxygen = oxygen_cylinders.objects.filter(district_id=dist[0])
	medicine = Medicines.objects.filter(district_id=dist[0])
	hosp_list = []
	ambulances_list = []
	oxygen_cylinder_list = []
	medical_store_list = []


	for i in hosp:
		w = {
		'name_of_hospital' : i.name_of_hospital
		}
		hosp_list.append(w)
		
		
	for i in ambu:
		w = {
		'vehicle_no_of_the_ambulance' : i.vehicle_no_of_the_ambulance
		}
		ambulances_list.append(w)
		
		
	for i in oxygen:
		w = {
		'name_of_the_oxygen_dealerame' : i.name_of_the_oxygen_dealer
		}
		oxygen_cylinder_list.append(w)
		
		
	for i in medicine:
		w = {
		'name_of_the_medical_store' : i.name_of_the_medical_store
		}
		medical_store_list.append(w)



	services={
		'hosp_list':hosp_list,
		'ambulances_list':ambulances_list,
  "oxygen_cylinder_list":oxygen_cylinder_list,
  "medical_store_list":medical_store_list, 
		'lst':lst
		}

		
	return render(request,'services.html',services)    





def hospital_list(request,name1,st,dt):
	states = State.objects.filter(state=st)
	dist = District.objects.filter(district=dt)
	hosp = Hospital.objects.filter(district_id=dist[0],name_of_hospital=name1)
	data = []

	for i in hosp:
		 data.append(i.name_of_hospital)
		 data.append(i.total_icu_beds)
		 data.append(i.total_icu_ventilator_beds)
		 data.append(i.total_o2_beds)
		 data.append(i.total_normal_beds)
		 data.append(i.contact_number_of_the_hospital)

	return render(request,'hospitals/hospitalList.html',{'data':data})



	
def ambulance_list(request,name1,st,dt):
	states = State.objects.filter(state=st)
	dist = District.objects.filter(district=dt)
	ambulance = Ambulances.objects.filter(district_id=dist[0],vehicle_no_of_the_ambulance=name1)
	data = []

	for i in ambulance:
		 data.append(i.name_of_the_ambulance_driver)
		 data.append(i.vehicle_no_of_the_ambulance)
		 data.append(i.contact_no_of_ambulance_driver)


	return render(request,'ambulances/ambulanceList.html',{'data':data})


def oxygen_cylinder_list(request,name1,st,dt):
	states = State.objects.filter(state=st)
	dist = District.objects.filter(district=dt)
	oxygen = oxygen_cylinders.objects.filter(district_id=dist[0],name_of_the_oxygen_dealer=name1)
	data = []

	for i in oxygen:
		 data.append(i.name_of_the_oxygen_dealer)
		 data.append(i.contact_no_of_the_oxygen_dealer)



	return render(request,'oxygenCylinders/oxygenCylinderList.html',{'data':data})	



def medical_store_list(request,name1,st,dt):
	states = State.objects.filter(state=st)
	dist = District.objects.filter(district=dt)
	medicine = Medicines.objects.filter(district_id=dist[0],name_of_the_medical_store=name1)
	data = []

	for i in medicine:
		 data.append(i.name_of_the_medical_store)
		 data.append(i.name_of_the_shop_owner)
		 data.append(i.contact_no_of_the_medical_shop_owner)


	return render(request,'medicalStores/medicalStoreList.html',{'data':data})	
