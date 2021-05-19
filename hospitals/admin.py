from django.contrib import admin

from .models import *

admin.site.register([State, District, Ambulances, oxygen_cylinders, Medicines, Hospital, History, StaffData, Reviews_hospital])
