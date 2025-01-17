from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.contrib import admin
from .models import *




class KeysInline(TranslationTabularInline,admin.TabularInline):
    model = Keys
    extra = 1


class Keys2Inline(TranslationTabularInline,admin.TabularInline):
    model = Keys2
    extra = 1


@admin.register(Statya)
class StatyaAdmin(TranslationAdmin):
    inlines = [KeysInline, Keys2Inline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class WhoForCoursInline(TranslationTabularInline, admin.TabularInline):
    model = WhoForCours
    extra = 1

class YouLearnInline(TranslationTabularInline,admin.TabularInline):
    model = YouLearn
    extra = 1

class ModuleInline(TranslationTabularInline,admin.TabularInline):
    model = Module
    extra = 1

@admin.register(Cours)
class CourseAdmin(TranslationAdmin):
    inlines = [WhoForCoursInline, YouLearnInline, ModuleInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class MaterialsInline(TranslationTabularInline,admin.TabularInline):
    model = Materials
    extra = 1

class ProgrammaMasterClassInline(TranslationTabularInline,admin.TabularInline):
    model = ProgrammaMasterClass
    extra = 1

class ProcessInline(admin.TabularInline):
    model = Process
    extra = 1


@admin.register(MasterClass)
class MasterClassAdmin(TranslationAdmin):
    inlines = [MaterialsInline, ProgrammaMasterClassInline, ProcessInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(FeedBack)
class FeedbackAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

# class FeedBackAdmin(admin.ModelAdmin):
#     list_display = ('client_name', 'date')
#     search_fields = ('client_name',)
#     list_filter = ('date',)

# admin.site.register(Statya, StatyaAdmin)
# admin.site.register(Cours, CourseAdmin)
# admin.site.register(MasterClass, MasterClassAdmin)
# admin.site.register(FeedBack, FeedBackAdmin)
