# Generated by Django 3.2.8 on 2021-11-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesnips', '0005_auto_20211109_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveddata',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saveddata',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
