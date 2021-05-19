from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from hospitals import views
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'state',views.StateViewSet)
router.register(r'district',views.DistrictViewSet)
router.register(r'hospital',views.HospitalViewSet)
router.register(r'ambulances',views.AmbulanceViewSet)
router.register(r'oxygen',views.OxygenViewSet)
router.register(r'medicines',views.MedicineViewSet)
router.register(r'history',views.HistoryViewSet)
router.register(r'staff',views.StaffViewSet)

next_page = None
urlpatterns = [
    path('api-auth/',include('rest_framework.urls',
        namespace='rest_framework')),
    path('',include(router.urls)),


    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
   
    
    url(r'services/(?P<id1>[A-Za-z0-9- ]+)/(?P<id2>[A-Za-z0-9- ]+)$',views.services, name='services'),

    url(r'hospital_list/(?P<name1>[A-Za-z0-9- ]+)/(?P<st>[A-Za-z0-9- ]+)/(?P<dt>[A-Za-z0-9- ]+)$', views.hospital_list,name='hosp_list'),
    url(r'ambulance_list/(?P<name1>[A-Za-z0-9- ]+)/(?P<st>[A-Za-z0-9- ]+)/(?P<dt>[A-Za-z0-9- ]+)$', views.ambulance_list,name='ambulance_list'),
    url(r'oxygen_cylinder_list/(?P<name1>[A-Za-z0-9- ]+)/(?P<st>[A-Za-z0-9- ]+)/(?P<dt>[A-Za-z0-9- ]+)$', views.oxygen_cylinder_list,name='oxygen_cylinder_list'),
    url(r'medical_store_lisst/(?P<name1>[A-Za-z0-9- ]+)/(?P<st>[A-Za-z0-9- ]+)/(?P<dt>[A-Za-z0-9- ]+)$', views.medical_store_list,name='medical_store_list'),


    url(r'all_hospitals_list/(?P<st>[A-Za-z0-9- ]+)/(?P<dt>[A-Za-z0-9- ]+)$', views.all_hospitals_list,name='all_hospitals_list'),
    url(r'all_ambulance_list/(?P<st>[A-Za-z0-9- ]+)/(?P<dt>[A-Za-z0-9- ]+)$', views.all_ambulance_list,name='all_ambulance_list'),
    url(r'all_oxygen_cylinders_list/(?P<st>[A-Za-z0-9- ]+)/(?P<dt>[A-Za-z0-9- ]+)$', views.all_oxygen_cylinders_list,name='all_oxygen_cylinders_list'),
    url(r'all_medical_sotres_list/(?P<st>[A-Za-z0-9- ]+)/(?P<dt>[A-Za-z0-9- ]+)$', views.all_medical_sotres_list,name='all_medical_sotres_list'),

    path('search', views.search, name='search'),
    path('', include('social_django.urls', namespace='social')),
    url(r'^logout$', LogoutView.as_view(),  name='logout'),
    #path('add/',views.add)
]


