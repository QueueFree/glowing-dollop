# Generated by Django 5.1.1 on 2024-10-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.IntegerField(default=0, max_length=2),
        ),
    ]
