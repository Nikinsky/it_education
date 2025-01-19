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

# class FeedBackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FeedBack
#         fields = ['id', 'client_name', 'image_client', 'text', 'date']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['course', 'master_class']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # Для отображения связанных CartItem

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']