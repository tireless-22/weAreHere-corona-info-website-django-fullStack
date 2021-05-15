from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
#    Hospital.objects.values('name_of_hospital','total_icu_beds','total_o2_beds','total_normal_beds','address').distinct()
# this line of code will create a list of dictonaries
# order_by will order according to alphabetical order of the passed element

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
		print(i.state)
		w[i.state] = []
		dist = District.objects.filter(state_id=i)
		#print(dist.district)
		for j in dist:
			w[i.state].append(j.district)
	print(w)

	return render(request,'hospitals/index.html',{'w':w})
def results(request):
    pass

def hospitals(request):
    obj = Hospital.objects.values('name_of_hospital','total_icu_beds','total_o2_beds','total_normal_beds','address').distinct()
    print(obj)
    return render(request,'hospitals/bedinfo.html',{'obj':obj})

# def list_of_hospitals(request,id1):
#     obj = Hospital.objects.filter(district=id1)
#     w={}
#     for i in obj:
#         w[i.name_of_hospital] = i.address
    
#     return render(request,'hospitals/hospitals.html',{'w':w})
# services we have to proovide the hospitals ,oxygen cylinders,ambulances and medical store details
def services(request,id1,id2):
	states = State.objects.filter(state=id1)
	#print(states[0].state)
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
		'name' : i.name_of_hospital
		}
		hosp_list.append(w)
	 

	return render(request,'services.html',{'hosp_list':hosp_list, 'lst':lst})    

def hosp_list(request,name1,st,dt):
	states = State.objects.filter(state=st)
	dist = District.objects.filter(district=dt)
	hosp = Hospital.objects.filter(district_id=dist[0],name_of_hospital=name1)
	data = []
	print(hosp)
	for i in hosp:
		 data.append(i.name_of_hospital)
		 data.append(i.total_icu_beds)
		 data.append(i.total_icu_ventilator_beds)
		 data.append(i.total_o2_beds)
		 data.append(i.total_normal_beds)
		 data.append(i.contact_number_of_the_hospital)

	return render(request,'hospitals/hosp_list.html',{'data':data})

