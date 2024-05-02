# Generated by Django 5.0.4 on 2024-05-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=60)),
                ('year_of_creation', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]