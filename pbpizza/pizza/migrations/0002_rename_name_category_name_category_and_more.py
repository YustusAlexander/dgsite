# Generated by Django 4.0.2 on 2022-03-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='name_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=0, max_length=50, verbose_name='Size'),
            preserve_default=False,
        ),
    ]