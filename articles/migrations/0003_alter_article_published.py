# Generated by Django 3.2.13 on 2022-05-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220523_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
    ]
