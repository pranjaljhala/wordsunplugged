# Generated by Django 3.0.4 on 2020-03-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_delete_quotes1'),
    ]

    operations = [
        migrations.CreateModel(
            name='sayings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('saying', models.TextField()),
            ],
        ),
    ]
