from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Photo

from .models import Biography, Period, ContentAtom, Memoir


class PeriodInline(admin.StackedInline):
    model = Period


class BiographyAdmin(admin.ModelAdmin):
    model = Biography
    save_on_top = True
    inlines = [
        PeriodInline,
    ]
    list_display = ('user', 'creator', 'modified')
    fieldsets = (
        (_("General"), {
            'fields': ('user', )
        }),
        (_("Birth"), {
            'fields': ('date_of_birth', 'place_of_birth')
        }),
        (_("Passing"), {
            'classes': ('collapse',),
            'fields': ('date_of_passing', 'place_of_passing')
        }),
    )

    def save_model(self, request, obj, form, change):
        ''' add the creator '''
        if not obj.created:
            obj.creator = request.user

        super().save_model(request, obj, form, change)


class MemoirInline(admin.StackedInline):
    model = Memoir


class PeriodAdmin(admin.ModelAdmin):
    model = Period
    inlines = [
        MemoirInline,
    ]


class ContentAtomAdmin(admin.ModelAdmin):
    model = ContentAtom
    list_display = ('placed', 'owner', 'who', 'date')
    inlines = [
        MemoirInline,
    ]

class PhotoAdmin(PhotoAdminDefault):
    readonly_fields = ()


admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)

admin.site.register(Biography, BiographyAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Memoir)
admin.site.register(ContentAtom, ContentAtomAdmin)
