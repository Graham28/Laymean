# Generated by Django 2.0.7 on 2019-05-14 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20190514_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.TextField(),
        ),
    ]
