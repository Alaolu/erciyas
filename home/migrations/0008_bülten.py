# Generated by Django 2.1.7 on 2020-12-14 16:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201214_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bülten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Bülten Başlık')),
                ('text', ckeditor.fields.RichTextField(null=True, verbose_name='Uzun İçerik')),
                ('image', models.ImageField(null=True, upload_to='fotolar/')),
            ],
        ),
    ]
