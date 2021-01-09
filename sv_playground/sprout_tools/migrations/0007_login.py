# Generated by Django 3.1.3 on 2021-01-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprout_tools', '0006_auto_20210107_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=15, unique=True, verbose_name='Login ID')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('created_at', models.DateTimeField(verbose_name='Создано')),
                ('updated_at', models.DateTimeField(verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Login',
                'verbose_name_plural': 'Logins',
            },
        ),
    ]
