from django.contrib import admin

from .models import Biography, Season, ContentAtom, Memoir


class SeassonInline(admin.StackedInline):
    model = Season


class BiographyAdmin(admin.ModelAdmin):
    model = Biography
    inlines = [
        SeassonInline,
    ]


class MemoirInline(admin.StackedInline):
    model = Memoir


class SeasonAdmin(admin.ModelAdmin):
    model = Season
    inlines = [
        MemoirInline,
    ]


admin.site.register(Biography, BiographyAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Memoir)
admin.site.register(ContentAtom)
