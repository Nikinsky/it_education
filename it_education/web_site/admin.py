from django.contrib import admin
from .models import *


class KeysInline(admin.TabularInline):
    model = Keys
    extra = 1


class Keys2Inline(admin.TabularInline):
    model = Keys2
    extra = 1

class StatyaAdmin(admin.ModelAdmin):
    inlines = [KeysInline,Keys2Inline]
    list_display = ('title', 'date')
    search_fields = ('title',)

class WhoForCoursInline(admin.TabularInline):
    model = WhoForCours
    extra = 1

class YouLearnInline(admin.TabularInline):
    model = YouLearn
    extra = 1

class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1

class CoursAdmin(admin.ModelAdmin):
    inlines = [WhoForCoursInline, YouLearnInline, ModuleInline]
    list_display = ('title', 'price', 'dostup_course')
    search_fields = ('title',)
    list_filter = ('dostup_course',)

class MaterialsInline(admin.TabularInline):
    model = Materials
    extra = 1

class ProgrammaMasterClassInline(admin.TabularInline):
    model = ProgrammaMasterClass
    extra = 1

class ProcessInline(admin.TabularInline):
    model = Process
    extra = 1

class MasterClassAdmin(admin.ModelAdmin):
    inlines = [MaterialsInline, ProgrammaMasterClassInline, ProcessInline]
    list_display = ('title', 'price', 'dostup')
    search_fields = ('title',)
    list_filter = ('dostup',)

class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'date')
    search_fields = ('client_name',)
    list_filter = ('date',)

admin.site.register(Statya, StatyaAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
