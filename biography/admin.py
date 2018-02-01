from django.contrib import admin

from .models import Biography, Season, ContentAtom, Memoir


class SeassonInline(admin.StackedInline):
    model = Season


class BiographyAdmin(admin.ModelAdmin):
    model = Biography
    inlines = [
        SeassonInline,
    ]
    list_display = ('user', 'creator', 'modified')


class MemoirInline(admin.StackedInline):
    model = Memoir


class SeasonAdmin(admin.ModelAdmin):
    model = Season
    inlines = [
        MemoirInline,
    ]


class ContentAtomAdmin(admin.ModelAdmin):
    model = ContentAtom
    list_display = ('placed', 'owner', 'who', 'date')


admin.site.register(Biography, BiographyAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Memoir)
admin.site.register(ContentAtom, ContentAtomAdmin)
