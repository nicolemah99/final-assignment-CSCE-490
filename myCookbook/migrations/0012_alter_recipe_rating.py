# Generated by Django 4.1.3 on 2022-12-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCookbook', '0011_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0, null=True),
        ),
    ]