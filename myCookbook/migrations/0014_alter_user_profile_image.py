# Generated by Django 4.1.3 on 2022-12-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCookbook', '0013_alter_recipe_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profileImages/default_profile.png', null=True, upload_to='images/profileImages/', verbose_name='Profile Image'),
        ),
    ]