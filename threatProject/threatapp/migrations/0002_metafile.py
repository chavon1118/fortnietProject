# Generated by Django 2.1.dev20180216185855 on 2018-02-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threatapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=128)),
                ('isImported', models.BooleanField()),
            ],
        ),
    ]