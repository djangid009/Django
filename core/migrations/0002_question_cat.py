# Generated by Django 3.0.2 on 2020-01-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_cat',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=100)),
            ],
        ),
    ]
