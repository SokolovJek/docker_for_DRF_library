# Generated by Django 2.2.24 on 2022-04-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20220420_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='is_active',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('DONE', 'done')], default='active', max_length=20),
        ),
    ]