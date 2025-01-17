from modeltranslation.translator import register, TranslationOptions
from .models import (
    Statya, Keys, Keys2, Cours, WhoForCours,
    YouLearn, Module, FeedBack, MasterClass,
    Materials, ProgrammaMasterClass, Process
)

@register(Statya)
class StatyaTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description1', 'description2', 'description3')

@register(Keys)
class KeysTranslationOptions(TranslationOptions):
    fields = ('key',)

@register(Keys2)
class Keys2TranslationOptions(TranslationOptions):
    fields = ('keys',)

@register(Cours)
class CoursTranslationOptions(TranslationOptions):
    fields = ('title', 'description1', 'description2', 'description3',
              'description4', 'description5', 'about_description', 'dostup_course')

@register(WhoForCours)
class WhoForCoursTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(YouLearn)
class YouLearnTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Module)
class ModuleTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(FeedBack)
class FeedBackTranslationOptions(TranslationOptions):
    fields = ('client_name', 'text')

@register(MasterClass)
class MasterClassTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'dostup', 'description_about_master_class',
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