# Generated by Django 3.1.7 on 2021-07-07 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestuser',
            name='message',
            field=models.TextField(),
        ),
    ]
