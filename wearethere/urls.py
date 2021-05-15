from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from hospitals import views

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

urlpatterns = [
    path('api-auth/',include('rest_framework.urls',
        namespace='rest_framework')),
    path('',include(router.urls)),
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    #path('hospitals/',views.hospitals, name='hospitals'),


    # url(r'list_of_hospitals/(?P<id1>[A-Za-z-]+)$',views.list_of_hospitals, name='list_of_hospitals'),
    url(r'services/(?P<id1>[A-Za-z- ]+)/(?P<id2>[A-Za-z- ]+)$',views.services, name='services'),
    url(r'hosp_list/(?P<name1>[A-Za-z]+)/(?P<st>[A-Za-z- ]+)/(?P<dt>[A-Za-z- ]+)$', views.hosp_list,name='hosp_list'),

    # testing purpose
    path('test/',views.services, name='hospitals'),

]
