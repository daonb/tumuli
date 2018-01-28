from django.contrib import admin
from biography.models import Biography, Season, ContentAtom, Memoir

# Register your models here.
admin.site.register(Biography)
admin.site.register(Season)
admin.site.register(Memoir)
admin.site.register(ContentAtom)
