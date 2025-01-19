from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django.contrib import admin
from .models import *

#
# class MainPageQuestionInlines(TranslationTabularInline, admin.TabularInline):
#     model = MainPageQuestions
#     extra = 1
#
#
# @admin.register(MainPage)
# class MainPageAdmin(TranslationAdmin):
#     inlines = [MainPageQuestionInlines]
#
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }
#
#

admin.site.register(UserProfile)

class KeysInline(TranslationTabularInline,admin.TabularInline):
    model = Keys
    extra = 0


class Keys2Inline(TranslationTabularInline,admin.TabularInline):
    model = Keys2
    extra = 0


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
    extra = 0

class YouLearnInline(TranslationTabularInline,admin.TabularInline):
    model = YouLearn
    extra = 0

class ModuleInline(TranslationTabularInline,admin.TabularInline):
    model = Module
    extra = 0

class Process_learnInlines(TranslationTabularInline, admin.TabularInline):
    model = Process_learn
    extra = 0


class IntoCourseInlines(TranslationTabularInline, admin.TabularInline):
    model = IntoCourse
    extra = 0


@admin.register(Cours)
class CourseAdmin(TranslationAdmin):
    inlines = [WhoForCoursInline, YouLearnInline, ModuleInline, Process_learnInlines, IntoCourseInlines]
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
    extra = 0

class ProgrammaMasterClassInline(TranslationTabularInline,admin.TabularInline):
    model = ProgrammaMasterClass
    extra = 0

class ProcessInline(TranslationTabularInline, admin.TabularInline):
    model = Process
    extra = 0



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



class TariffInfoInlines(TranslationTabularInline, admin.TabularInline):
    model = TariffInfo
    extra = 0


@admin.register(Tariff)
class TariffClassAdmin(TranslationAdmin):
    inlines = [TariffInfoInlines]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(VisaCart)
admin.site.register(Feedback)
admin.site.register(PodpiskiUser)
admin.site.register(Cart)
admin.site.register(CartItem)





# admin.site.register(Statya, StatyaAdmin)
# admin.site.register(Cours, CourseAdmin)
# admin.site.register(MasterClass, MasterClassAdmin)
# admin.site.register(FeedBack, FeedBackAdmin)
