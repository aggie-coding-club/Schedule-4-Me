# Generated by Django 3.1.6 on 2021-03-10 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule4me', '0006_auto_20210114_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.IntegerField(primary_key=True, serialize=False)),
                ('schedule_name', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]
