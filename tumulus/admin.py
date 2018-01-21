from django.contrib import admin
from tumulus.models import Tumulus, Season, MemoryDump, PersonalDump

# Register your models here.
admin.site.register(Tumulus)
admin.site.register(Season)
admin.site.register(MemoryDump)
admin.site.register(PersonalDump)
