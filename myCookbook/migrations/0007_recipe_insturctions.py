# Generated by Django 4.1.3 on 2022-12-02 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCookbook', '0006_alter_recipe_min_alter_recipe_num_servings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='insturctions',
            field=models.TextField(null=True),
        ),
    ]