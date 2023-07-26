# Generated by Django 4.2.3 on 2023-07-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaccounts',
            name='from_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='emailaccounts',
            name='from_warmup_emails_sent',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
