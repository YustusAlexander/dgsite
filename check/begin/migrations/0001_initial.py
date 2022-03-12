# Generated by Django 4.0.2 on 2022-03-08 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Begin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('number', models.IntegerField()),
                ('photo', models.ImageField(upload_to='image/')),
            ],
        ),
    ]