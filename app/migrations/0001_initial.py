# Generated by Django 3.2.6 on 2021-08-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noohin_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noo_name', models.CharField(max_length=200)),
            ],
        ),
    ]
