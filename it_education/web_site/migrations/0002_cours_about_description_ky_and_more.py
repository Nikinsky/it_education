# Generated by Django 5.1.5 on 2025-01-17 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='about_description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='about_description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description1_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description1_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description2_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description2_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description3_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description3_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description4_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description4_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description5_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description5_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='dostup_course_ky',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='dostup_course_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='title_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='client_name_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='client_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='text_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='keys',
            name='key_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='keys',
            name='key_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='keys2',
            name='keys_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='keys2',
            name='keys_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='description_about_master_class_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='description_about_master_class_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='description_process_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='description_process_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='dostup_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='dostup_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='position_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='position_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='title_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='materials',
            name='name_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='materials',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='title_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='programmamasterclass',
            name='name_master_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='programmamasterclass',
            name='name_master_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='description1_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='description1_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='description2_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='description2_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='description3_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='description3_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='title_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='statya',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='whoforcours',
            name='name_ky',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='whoforcours',
            name='name_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='youlearn',
            name='name_ky',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='youlearn',
            name='name_ru',
            field=models.CharField(max_length=500, null=True),
        ),
    ]