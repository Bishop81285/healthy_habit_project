# Generated by Django 4.2.7 on 2023-11-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='id пользователя telegram'),
        ),
    ]
