# Generated by Django 4.1 on 2022-09-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=50)),
                ('postal_code', models.BigIntegerField()),
                ('address_name', models.CharField(max_length=50)),
                ('address_line1', models.CharField(max_length=50)),
                ('address_line2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('landmark', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Adress',
        ),
    ]
