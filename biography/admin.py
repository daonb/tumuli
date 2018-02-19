from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Biography, Period, ContentAtom, Memoir
from .forms import StoryAudioForm


class PeriodInline(admin.StackedInline):
    model = Period


class BiographyAdmin(admin.ModelAdmin):
    model = Biography
    form = StoryAudioForm
    inlines = [
        PeriodInline,
    ]
    list_display = ('user', 'creator', 'modified')
    fieldsets = (
        (_("Birth"), {
            'fields': ('date_of_birth', 'place_of_birth')
        }),
        (_("Passing"), {
            'classes': ('collapse',),
            'fields': ('date_of_passing', 'place_of_passing')
        }),
    )


class MemoirInline(admin.StackedInline):
    model = Memoir
    form = StoryAudioForm


class PeriodAdmin(admin.ModelAdmin):
    model = Period
    form = StoryAudioForm
    inlines = [
        MemoirInline,
    ]


class ContentAtomAdmin(admin.ModelAdmin):
    model = ContentAtom
    list_display = ('placed', 'owner', 'who', 'date')
    inlines = [
        MemoirInline,
    ]


admin.site.register(Biography, BiographyAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Memoir)
admin.site.register(ContentAtom, ContentAtomAdmin)
