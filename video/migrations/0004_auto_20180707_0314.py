# Generated by Django 2.0.4 on 2018-07-07 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_videocomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videocomment',
            old_name='post',
            new_name='video',
        ),
    ]
