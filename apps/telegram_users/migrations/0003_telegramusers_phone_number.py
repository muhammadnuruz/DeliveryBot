# Generated by Django 5.0.1 on 2025-04-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0002_alter_telegramusers_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramusers',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
