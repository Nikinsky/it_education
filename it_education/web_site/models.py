from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail







#
# class MainPage(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#
#
# class MainPageQuestions(models.Model):
#     main_page = models.ForeignKey(MainPage, related_name='keys_main_page', on_delete=models.CASCADE)
#     question = models.CharField(max_length=250)
#     answer = models.TextField()
#
#
# class Tariff(models.Model):
#     TERM_CHOICES = (
#         ('месяц +', 'месяц +'),
#         ('год', 'год'),
#         ('год+', 'год+'),
#     )
#     term_status = models.CharField(max_length=32, choices=TERM_CHOICES, default='месяц +')
#     sum = models.PositiveIntegerField
#     TARIFF_PAY = (
#         ("Ежемесячно", "Ежемесячно"),
#         ("Ежегодно", "Ежегодно"),
#     )
#     tariff_pay = models.CharField(max_length=32, choices=TARIFF_PAY, default='Ежемесячно')
#
#
# class TariffInfo(models.Model):
#     tariff =models.ForeignKey(Tariff, related_name='tariff_info', on_delete=models.CASCADE)
#     info = models.CharField(max_length=100)
#
#
# class QuestionTariff(models.Model):
#     tariff = models.ForeignKey(Tariff, related_name='question_tariff', on_delete=models.CASCADE)
#     question = models.CharField(max_length=250)
#     answer = models.TextField()

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True,blank=True)
    GENDER = (
        ('Мужской','Мужской'),
        ('Женский', 'Женский'),
    )
    gender_status = models.CharField(max_length=32, choices=GENDER, null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    country = models.CharField(max_length=50, null=True,blank=True)
    city = models.CharField(max_length=50, null=True,blank=True)
    position = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return f'{self.username}'





class Statya(models.Model):
    title = models.CharField(max_length=255)
    description =models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='statya_images/')
    description1 = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

class Keys(models.Model):
    statya = models.ForeignKey(Statya, related_name='keys_statya', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)

    def __str__(self):
        return self.key

class Keys2(models.Model):
    statya = models.ForeignKey(Statya, related_name='keys_statya2', on_delete=models.CASCADE)
    keys = models.CharField(max_length=255)

class Cours(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    dostup_course = models.CharField(max_length=250)
    modul = models.TextField(null=True, blank=True)
    material = models.TextField(null=True, blank=True)
    description4 = models.TextField(null=True, blank=True)
    description5 = models.TextField(null=True, blank=True)
    about_description = models.TextField(null=True, blank=True)
    image_prepod = models.ImageField(upload_to='course_img/')
    full_name = models.CharField(max_length=50,null=True, blank=True)
    position = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.title


class WhoForCours(models.Model):
    name = models.CharField(max_length=500)
    course = models.ForeignKey(Cours, related_name='who_for_course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class YouLearn(models.Model):
    name = models.CharField(max_length=500)
    course = models.ForeignKey(Cours, related_name='you_learns', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Module(models.Model):
    module_num = models.CharField(max_length=15)
    description = models.TextField()
    course = models.ForeignKey(Cours, related_name='modules', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.module_num}: {self.course.title}"





class MasterClass(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField( null=True, blank=True)
    dostup = models.CharField(max_length=255, null=True, blank=True)
    count_lesson = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description_about_master_class = models.TextField( null=True, blank=True)
    image_master = models.ImageField(upload_to='master_class_images/', null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    description_process = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.title


class Materials(models.Model):
    master_class = models.ForeignKey(MasterClass, related_name='materials', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProgrammaMasterClass(models.Model):
    name_master = models.CharField(max_length=255)
    master_class = models.ForeignKey(MasterClass, related_name='programma_master_classes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_master


class Process(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    master_class = models.ForeignKey(MasterClass, related_name='master_classes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, related_name='carts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Cours, related_name='course_item', on_delete=models.CASCADE, null=True, blank=True)
    master_class = models.ForeignKey(MasterClass, related_name='master_class_item', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.cart}"

#jwt
# забыли пароль
#
#курс post (tocket)
#master_cart(post)


