# Generated by Django 2.2.16 on 2020-10-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
                ('desc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
