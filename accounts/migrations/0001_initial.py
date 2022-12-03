# Generated by Django 4.0.1 on 2022-01-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('libraryId', models.CharField(max_length=100)),
                ('bookTitle', models.CharField(max_length=200)),
                ('dateOut', models.DateField()),
                ('dueDate', models.DateField()),
                ('due', models.IntegerField()),
            ],
        ),
    ]