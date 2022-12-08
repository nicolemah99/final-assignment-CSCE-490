# Generated by Django 4.1.3 on 2022-12-08 00:59

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myCookbook', '0020_remove_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique_with=('author',)),
        ),
    ]
