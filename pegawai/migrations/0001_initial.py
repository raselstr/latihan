# Generated by Django 3.2 on 2021-04-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pegawai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=18)),
                ('nama', models.CharField(max_length=25)),
                ('jabatan', models.CharField(max_length=50)),
            ],
        ),
    ]