from django.contrib import admin
from .models import Hydrant, Reservoir, check_up_hydrant, check_up_reservoir

# Register your models here.
admin.site.register(Hydrant)
admin.site.register(Reservoir)
admin.site.register(check_up_hydrant)
admin.site.register(check_up_reservoir)

