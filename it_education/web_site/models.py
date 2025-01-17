from django.db import models

class Statya(models.Model):
    title = models.CharField(max_length=255)
    description =models.TextField()
    image = models.ImageField(upload_to='statya_images/')
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    date = models.DateField()


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
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dostup_course = models.CharField(max_length=250)
    modul = models.TextField()
    material = models.TextField()
    description4 = models.TextField()
    description5 = models.TextField()
    about_description = models.TextField()
    image_prepod = models.ImageField(upload_to='course_img/')
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

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

class FeedBack(models.Model):
    client_name = models.CharField(max_length=255)
    image_client = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.client_name

class MasterClass(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    dostup = models.CharField(max_length=255)
    count_lesson = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description_about_master_class = models.TextField()
    image_master = models.ImageField(upload_to='master_class_images/')
    position = models.CharField(max_length=255)
    description_process = models.TextField()

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
