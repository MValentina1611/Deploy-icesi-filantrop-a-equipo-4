# Generated by Django 4.2.5 on 2023-09-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmModule', '0002_alter_sponsor_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='personType',
            field=models.CharField(choices=[('N', 'NATURAL'), ('J', 'JURIDICA')], max_length=1),
        ),
    ]
