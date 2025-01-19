from rest_framework import serializers
from .models import *



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'gender_status', 'birthday', 'country', 'city', 'position']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_new_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        """
        Проверка совпадения нового пароля и его подтверждения.
        """
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')

        if new_password != confirm_new_password:
            raise serializers.ValidationError({'confirm_new_password': 'New passwords do not match.'})

        # Дополнительные проверки сложности пароля
        if len(new_password) < 8:
            raise serializers.ValidationError({'new_password': 'Password must be at least 8 characters long.'})
        if not any(char.isdigit() for char in new_password):
            raise serializers.ValidationError({'new_password': 'Password must contain at least one digit.'})
        if not any(char.isalpha() for char in new_password):
            raise serializers.ValidationError({'new_password': 'Password must contain at least one letter.'})

        return data

#
# class ResetPasswordEmailSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)

class ResetPasswordConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)


class ResetPasswordEmailSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(write_only=True)
    class Meta:
        model = UserProfile
        fields = ['email']
    def validate_email(self, value):
        """
        Проверка, существует ли пользователь с таким email.
        """
        if not UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email не найден.")
        return value


class ResetPasswordConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True, max_length=16, min_length=8)

    def validate_password(self, value):
        # Дополнительные проверки на сложность пароля (опционально)
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен содержать не менее 8 символов.")
        return value







class UserProfileFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'image']



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['fio', 'image', 'phone_number', 'gender_status', 'birthday', 'country', 'city', 'position' ]




class VisaCartSerializer(serializers.ModelSerializer):
    graduation_date = serializers.DateField(format=('%M-%Y'))
    class Meta:
        model = VisaCart
        fields = ['number_cart', 'graduation_date',]


class VisaCartPodpiskiSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaCart
        fields = ['number_cart',]


class TariffInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffInfo
        fields = ['id', 'info']



class TariffListSerializer(serializers.ModelSerializer):
    tariff_info = TariffInfoSerializer(many=True, read_only=True)
    class Meta:
        model = Tariff
        fields = ['id', 'term_status', 'sum', 'tariff_pay', 'tariff_info']



class TariffForCartSerializer(serializers.ModelSerializer):
    tariff_info = TariffInfoSerializer(many=True, read_only=True)
    class Meta:
        model = Tariff
        fields = ['term_status', 'status', 'sum',]









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

class StatyaPosleSerializer(serializers.ModelSerializer):
    keys_statya = KeysSerializer(many=True, read_only=True)
    keys_statya2 = Keys2Serializer(many=True, read_only=True)

    class Meta:
        model = Statya
        fields = ['id', 'title', 'description',  'date', 'image', 'keys_statya','description1', 'description2', 'description3', 'keys_statya2']

class StatyaDoSerializer(serializers.ModelSerializer):
    keys_statya = KeysSerializer(many=True, read_only=True)

    class Meta:
        model = Statya
        fields = ['id', 'title', 'description',  'date', 'image', 'for_key_description', 'keys_statya',]











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



class ProcessLearnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process_learn
        fields = ['id', 'number', 'title', 'description']

class IntoCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntoCourse
        fields = ['material']



class CoursDetailSerializer(serializers.ModelSerializer):
    who_for_course = WhoForCoursSerializer(many=True, read_only=True)
    you_learns = YouLearnSerializer(many=True, read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)
    course_pl = ProcessLearnSerializer(many=True, read_only=True)
    into_course = IntoCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Cours
        fields = ['id', 'title', 'description','into_course', 'description1', 'description2', 'description3', 'price', 'dostup_course',
                  'modul', 'material', 'description4', 'description5', 'image_prepod',
                  'full_name', 'position', 'who_for_course', 'you_learns', 'modules', 'course_pl']



class CoursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ['id', 'title', 'about_description']









class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ['name']

class ProgrammaMasterClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammaMasterClass
        fields = ['name_master']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['title', 'description']



class MasterClassDetailSerializer(serializers.ModelSerializer):
    materials = MaterialsSerializer(many=True, read_only=True)
    programma_master_classes = ProgrammaMasterClassSerializer(many=True, read_only=True)
    master_classes = ProcessSerializer(many=True, read_only=True)
    class Meta:
        model = MasterClass
        fields = ['id', 'title', 'description', 'dostup', 'into_master', 'count_lesson', 'price', 'description_about_master_class',
                  'image_master', 'position', 'description_process', 'materials', 'programma_master_classes', 'master_classes']


class MasterClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterClass
        fields = ['id', 'title', 'price', 'dostup']








class FeedBackSerializer(serializers.ModelSerializer):
    user = UserProfileFeedbackSerializer(many=True, read_only=True)
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'text', 'created_date']






class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['course', 'master_class']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # Для отображения связанных CartItem

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']



class PodpiskiSerializer(serializers.ModelSerializer):
    tariff = TariffForCartSerializer()
    visa_cart = VisaCartPodpiskiSerializer()
    srok = serializers.DateField(format=('%D-%M-%Y'))
    class Meta:
        model = PodpiskiUser
        fields = ['tariff', 'visa_cart', 'srok']