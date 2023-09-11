# Generated by Django 4.2.5 on 2023-09-11 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('contact_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('previousColab', models.CharField(max_length=200)),
                ('personType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmModule.event_type')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participation', models.CharField(max_length=100)),
                ('Sponsor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmModule.sponsor')),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmModule.event')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateField(unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('officiaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmModule.official')),
                ('sponsorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmModule.sponsor')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmModule.event_type'),
        ),
    ]
