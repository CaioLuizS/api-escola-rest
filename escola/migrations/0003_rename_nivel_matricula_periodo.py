# Generated by Django 5.0.3 on 2024-09-16 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matricula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='nivel',
            new_name='periodo',
        ),
    ]
