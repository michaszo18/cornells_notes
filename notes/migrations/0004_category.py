# Generated by Django 3.1.5 on 2021-01-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
