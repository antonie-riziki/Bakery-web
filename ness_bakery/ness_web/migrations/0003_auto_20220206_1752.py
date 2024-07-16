# Generated by Django 3.1.3 on 2022-02-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ness_web', '0002_graduationcake'),
    ]

    operations = [
        migrations.CreateModel(
            name='BabyShowerCake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('image', models.FileField(upload_to='img')),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BirthdayCake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('image', models.FileField(upload_to='img')),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CupCake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('image', models.FileField(upload_to='img')),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThemedCake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('image', models.FileField(upload_to='img')),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeddingCake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('image', models.FileField(upload_to='img')),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='graduationcake',
            old_name='gc_name',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='graduationcake',
            old_name='gc_img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='graduationcake',
            old_name='gc_price',
            new_name='price',
        ),
    ]
