from rest_framework import serializers
from .models import *



class Keys2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Keys2
        fields = ['id', 'keys']

class KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keys
        fields = ['id', 'key']

class StatyaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statya
        fields = ['id', 'title', 'date', 'image']

class StatyaDetailSerializer(serializers.ModelSerializer):
    keys_statya = KeysSerializer(many=True, read_only=True)
    keys_statya2 = Keys2Serializer(many=True, read_only=True)

    class Meta:
        model = Statya
        fields = ['id', 'title', 'date', 'image', 'description1', 'description2', 'keys_statya','keys_statya2']

class WhoForCoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoForCours
        fields = ['id', 'name']

class YouLearnSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLearn
        fields = ['id', 'name']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'module_num', 'description']

class CoursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ['id', 'title', 'about_description']

class CoursDetailSerializer(serializers.ModelSerializer):
    who_for_course = WhoForCoursSerializer(many=True, read_only=True)
    you_learns = YouLearnSerializer(many=True, read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Cours
        fields = ['id', 'title', 'description1', 'description2', 'description3', 'price', 'dostup_course',
                  'modul', 'material', 'description4', 'description5', 'about_description', 'image_prepod',
                  'full_name', 'position', 'who_for_course', 'you_learns', 'modules']

class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ['id', 'name']

class ProgrammaMasterClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammaMasterClass
        fields = ['id', 'name_master']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id', 'title', 'description']

class MasterClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClass
        fields = ['id', 'title', 'price', 'dostup']

class MasterClassDetailSerializer(serializers.ModelSerializer):
    materials = MaterialsSerializer(many=True, read_only=True)
    programma_master_classes = ProgrammaMasterClassSerializer(many=True, read_only=True)
    master_classes = ProcessSerializer(many=True, read_only=True)

    class Meta:
        model = MasterClass
        fields = ['id', 'title', 'description', 'dostup', 'count_lesson', 'price', 'description_about_master_class',
                  'image_master', 'position', 'description_process', 'materials', 'programma_master_classes', 'master_classes']

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['id', 'client_name', 'image_client', 'text', 'date']
