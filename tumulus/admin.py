from django.contrib import admin
from tumulus.models import Tumulus, Season, MemoryDump, Memoir

# Register your models here.
admin.site.register(Tumulus)
admin.site.register(Season)
admin.site.register(Memoir)
admin.site.register(MemoryDump)
