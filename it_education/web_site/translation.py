from modeltranslation.translator import register, TranslationOptions
from .models import (
    Statya, Keys, Keys2, Cours, WhoForCours,
    YouLearn, Module, MasterClass,
    Materials, ProgrammaMasterClass, Process, TariffInfo,Process_learn, IntoCourse,Tariff
)


@register(Tariff)
class TariffTranslationOptions(TranslationOptions):
    fields = []

@register(TariffInfo)
class TariffInfoTranslationOptions(TranslationOptions):
    fields = ('info',)


@register(Statya)
class StatyaTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description1', 'description2', 'description3', 'for_key_description')

@register(Keys)
class KeysTranslationOptions(TranslationOptions):
    fields = ('key',)

@register(Keys2)
class Keys2TranslationOptions(TranslationOptions):
    fields = ('keys',)

@register(Cours)
class CoursTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description1', 'description2', 'description3',
              'description4', 'description5', 'dostup_course', 'full_name', 'position')

@register(WhoForCours)
class WhoForCoursTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(YouLearn)
class YouLearnTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Module)
class ModuleTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Process_learn)
class Process_learnTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(IntoCourse)
class IntoCourseTranslationOptions(TranslationOptions):
    fields = ('material',)

@register(MasterClass)
class MasterClassTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'dostup', 'count_lesson', 'description_about_master_class',
              'position', 'description_process')

@register(Materials)
class MaterialsTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ProgrammaMasterClass)
class ProgrammaMasterClassTranslationOptions(TranslationOptions):
    fields = ('name_master',)

@register(Process)
class ProcessTranslationOptions(TranslationOptions):
    fields = ('title', 'description')