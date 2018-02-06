from django.contrib import admin

from .models import Biography, Period, ContentAtom, Memoir


class PeriodInline(admin.StackedInline):
    model = Period


class BiographyAdmin(admin.ModelAdmin):
    model = Biography
    inlines = [
        PeriodInline,
    ]
    list_display = ('user', 'creator', 'modified')


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


admin.site.register(Biography, BiographyAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Memoir)
admin.site.register(ContentAtom, ContentAtomAdmin)
