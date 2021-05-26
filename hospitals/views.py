from django.shortcuts import render
from django.http import HttpResponse 
from django.db.models.query import QuerySet
from .models import *
from rest_framework import viewsets
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


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
 data=[]
 w = {}
 for i in states:
  data1 = []
  data1.append(i.id)
  data1.append(i.state)
  data.append(data1)
  w[i.state] = []
  dist = District.objects.filter(state_id=i)
  for j in dist:
   lst = []
   lst.append(j.district)
   lst.append(j.dist_img)
   w[i.state].append(lst)
 print(w)
 return render(request,'index.html',{'w':w,'data':data})




def services(request,id1,id2):
 #print(id1,id2)
 states = State.objects.filter(state=id1)
 #print(states)
 dist = District.objects.filter(district=id2)
 lst = []
 lst.append(states[0].state)
 lst.append(dist[0].district)
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
  'name_of_hospital' : i.name_of_hospital,
  'hosp_img':i.hosp_img
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



# *********************************************************

def all_hospitals_list(request,st,dt):
 states = State.objects.filter(state=st)
 dist = District.objects.filter(district=dt)
 hosp = Hospital.objects.filter(district_id=dist[0])
 print(hosp)
 data = []
 data2=[]
 for i in hosp:
  data=[]
  data.append(i.name_of_hospital)
  data.append(i.total_icu_beds)
  data.append(i.total_icu_ventilator_beds)
  data.append(i.total_o2_beds)
  data.append(i.total_normal_beds)
  data.append(i.contact_number_of_the_hospital)
  data.append(i.pincode)
  data.append(i.address)
  data.append(i.gmap_link)
  print(data)
  


  data2.append(data)
 return render(request,'hospitals/allHospitalsList.html',{'data2':data2})

def all_ambulance_list(request,st,dt):
 states = State.objects.filter(state=st)
 dist = District.objects.filter(district=dt)
 ambs = Ambulances.objects.filter(district_id=dist[0])
 data = []
 data2=[]
 for i in ambs:
  data=[]
  data.append(i.vehicle_no_of_the_ambulance)
  data.append(i.name_of_the_ambulance_driver)
  data.append(i.contact_no_of_ambulance_driver)
  data.append(i.pincode)
  data.append(i.address)
  data.append(i.gmap_link)	
  data2.append(data)
 return render(request,'ambulances/allAmbulancesList.html',{'data2':data2})


def all_oxygen_cylinders_list(request,st,dt):
 states = State.objects.filter(state=st)
 dist = District.objects.filter(district=dt)
 oxys = oxygen_cylinders.objects.filter(district_id=dist[0])
 data = []
 data2=[]
 for i in oxys:
  data=[]
  data.append(i.name_of_the_oxygen_dealer)
  data.append(i.contact_no_of_the_oxygen_dealer)
  data.append(i.pincode)
  data.append(i.address)
  data.append(i.gmap_link)	
  data2.append(data)
 return render(request,'oxygenCylinders/allOxygenCylinderList.html',{'data2':data2})


def all_medical_sotres_list(request,st,dt):
 states = State.objects.filter(state=st)
 dist = District.objects.filter(district=dt)
 med = Medicines.objects.filter(district_id=dist[0])
 data = []
 data2=[]
 for i in med:
  data=[]
  data.append(i.name_of_the_medical_store)
  data.append(i.name_of_the_shop_owner)
  data.append(i.contact_no_of_the_medical_shop_owner)
  data.append(i.pincode)
  data.append(i.address)
  data.append(i.gmap_link)
  data2.append(data)
 return render(request,'medicalStores/allMedicalStoresList.html',{'data2':data2})			




#****************************************************************

def hospital_list(request,name1,st,dt):
 states = State.objects.filter(state=st)
 dist = District.objects.filter(district=dt)
 hosp = Hospital.objects.filter(district_id=dist[0],name_of_hospital=name1)
 rating = Reviews_hospital.objects.filter(hospital_id=hosp[0])
 reviews = []
 rates = []
 if rating:
  for i in rating:
   w = []
   w.append(i.username)
   w.append(range(i.rating))
   w.append(i.feedback)

   reviews.append(w)
  five_rating = Reviews_hospital.objects.filter(hospital_id=hosp[0],rating=5)
  four_rating = Reviews_hospital.objects.filter(hospital_id=hosp[0],rating=4)
  three_rating = Reviews_hospital.objects.filter(hospital_id=hosp[0],rating=3)
  two_rating = Reviews_hospital.objects.filter(hospital_id=hosp[0],rating=2)
  one_rating = Reviews_hospital.objects.filter(hospital_id=hosp[0],rating=1)
  total = len(five_rating)+len(four_rating)+len(three_rating)+len(two_rating)+len(one_rating)
  one = (len(one_rating)*100//total)
  two = (len(two_rating)*100//total)
  three = (len(three_rating)*100//total)
  four = (len(four_rating)*100//total)
  five = (len(five_rating)*100//total)
  rates.append([1,one])
  rates.append([2,two])
  rates.append([3,three]) 
  rates.append([4,four])
  rates.append([5,five])
  
 else:
   w = []
   w.append('Anonymous')
   w.append(range(5))
   w.append('Good response')

   reviews.append(w)
  
 

 data = []
 for i in hosp:
  data.append(i.name_of_hospital)
  data.append(i.total_icu_beds)
  data.append(i.total_icu_ventilator_beds)
  data.append(i.total_o2_beds)
  data.append(i.total_normal_beds)
  data.append(i.contact_number_of_the_hospital)
  data.append(i.pincode)
  data.append(i.address)
  data.append(i.gmap_link)
  data.append(i.hosp_img)
 return render(request,'hospitals/hospitalList.html',{'data':data,'reviews':reviews,'rates':rates})



 
def ambulance_list(request,name1,st,dt):
 states = State.objects.filter(state=st)
 rates=[]
 dist = District.objects.filter(district=dt)
 ambulance = Ambulances.objects.filter(district_id=dist[0],vehicle_no_of_the_ambulance=name1)
 print(ambulance)
 rating = Reviews_ambulance.objects.filter(ambulance_id=ambulance[0])
 reviews = []
 if rating:
  for i in rating:
   w = []
   w.append(i.username)
   w.append(range(i.rating))
   w.append(i.feedback)
   reviews.append(w)

  five_rating = Reviews_ambulance.objects.filter(ambulance_id=ambulance[0],rating=5)
  four_rating = Reviews_hospital.objects.filter(ambulance_id=ambulance[0],rating=4)
  three_rating = Reviews_hospital.objects.filter(ambulance_id=ambulance[0],rating=3)
  two_rating = Reviews_hospital.objects.filter(ambulance_id=ambulance[0],rating=2)
  one_rating = Reviews_hospital.objects.filter(ambulance_id=ambulance[0],rating=1)
  total = len(five_rating)+len(four_rating)+len(three_rating)+len(two_rating)+len(one_rating)
  one = (len(one_rating)*100//total)
  two = (len(two_rating)*100//total)
  three = (len(three_rating)*100//total)
  four = (len(four_rating)*100//total)
  five = (len(five_rating)*100//total)
  rates.append([1,one])
  rates.append([2,two])
  rates.append([3,three]) 
  rates.append([4,four])
  rates.append([5,five])
    
 else:
   w = []
   w.append('Anonymous')
   w.append(range(5))
   w.append('Good response')

   reviews.append(w)

 data = []

 for i in ambulance:
   data.append(i.name_of_the_ambulance_driver)
   data.append(i.vehicle_no_of_the_ambulance)
   data.append(i.contact_no_of_ambulance_driver)
   data.append(i.pincode)
   data.append(i.address)
   data.append(i.gmap_link)
 print(data) 
 return render(request,'ambulances/ambulanceList.html',{'data':data,'reviews':reviews})


def oxygen_cylinder_list(request,name1,st,dt):
 states = State.objects.filter(state=st)
 dist = District.objects.filter(district=dt)
 oxygen = oxygen_cylinders.objects.filter(district_id=dist[0],name_of_the_oxygen_dealer=name1)
 print(oxygen)
 data = []

 for i in oxygen:
   data.append(i.name_of_the_oxygen_dealer)
   data.append(i.contact_no_of_the_oxygen_dealer)
   data.append(i.pincode)
   data.append(i.address)
   data.append(i.gmap_link)
 return render(request,'oxygenCylinders/oxygenCylinderList.html',{'data':data})	



def medical_store_list(request,name1,st,dt):
 states = State.objects.filter(state=st)
 rates=[]
 dist = District.objects.filter(district=dt)
 medicine = Medicines.objects.filter(district_id=dist[0],name_of_the_medical_store=name1)
 rating = Reviews_medical_store.objects.filter(medical_store_id=medicine[0])
 reviews = []
 if rating:
  for i in rating:
   w = []
   w.append(i.username)
   w.append(range(i.rating))
   w.append(i.feedback)

   reviews.append(w)
  five_rating = Reviews_ambulance.objects.filter(medical_store_id=medicine[0],rating=5)
  four_rating = Reviews_hospital.objects.filter(medical_store_id=medicine[0],rating=4)
  three_rating = Reviews_hospital.objects.filter(medical_store_id=medicine[0],rating=3)
  two_rating = Reviews_hospital.objects.filter(medical_store_id=medicine[0],rating=2)
  one_rating = Reviews_hospital.objects.filter(medical_store_id=medicine[0],rating=1)
  total = len(five_rating)+len(four_rating)+len(three_rating)+len(two_rating)+len(one_rating)
  one = (len(one_rating)*100//total)
  two = (len(two_rating)*100//total)
  three = (len(three_rating)*100//total)
  four = (len(four_rating)*100//total)
  five = (len(five_rating)*100//total)
  rates.append([1,one])
  rates.append([2,two])
  rates.append([3,three]) 
  rates.append([4,four])
  rates.append([5,five])
    
 else:
   w = []
   w.append('Anonymous')
   w.append(range(5))
   w.append('Good response')

   reviews.append(w)


 data = []
 
 for i in medicine:
   data.append(i.name_of_the_medical_store)
   data.append(i.name_of_the_shop_owner)
   data.append(i.contact_no_of_the_medical_shop_owner)
   data.append(i.pincode)
   data.append(i.address)
   data.append(i.gmap_link)
 

 return render(request,'medicalStores/medicalStoreList.html',{'data':data,'reviews':reviews})	



# def ddl(request):
#   stateObj=State.objects.all()
#   districtObj=District.objects.all()
#   data=[]
#   for i in districtObj:
#     data.append(i.state)
#   print(data)  



  

#   return render(request,'dropDown.html',{"states":stateObj,"districts":districtObj})
  
@csrf_exempt
def getValues(request):
  if request.method == 'POST':
    state = request.POST.get("key")
    dist = request.POST.get("j")
    
    state = State.objects.filter(id=state)
    dist = District.objects.filter(id=dist)
    print(state[0].state,dist[0].district)
    return services(request,id1=state[0].state,id2=dist[0].district)


'''def ddl(request):
  stateObj=State.objects.all()
  districtObj=District.objects.all()
  data=[]
  data1=[]
  data2=[]

  #print(districtObj)
  for i in districtObj:
    data=[]
    #print(i.state)
    #print(i.district)
    data.append(i)
    data.append(i.state)
    data.append(i.district)
    print(data)
    data1.append(data)
  #print(data1)
  #print('States:',stateObj)

  for i in stateObj:
    data2.append(i.state) 
  #print(data2)
  #print(stateObj)
  context={
    "stateObj":stateObj,
    "data1":data1,
    "data2":data2,
  }

  return render(request,'dropDown.html',context)  
'''
'''@csrf_exempt
def ddl(request):
  state = State.objects.all()
  data = []
  for i in state:
    data1 = []
    data1.append(i.id)
    data1.append(i.state)
    data.append(data1)
  return render(request, 'dropDown.html', {'data':data})'''

def get_districts_ajax(request):
  if request.method=="POST":
    subject_id = request.POST['subject_id']
    dist = District.objects.filter(state_id=subject_id)

    return JsonResponse(list(dist.values('id', 'district')), safe = False) 
 