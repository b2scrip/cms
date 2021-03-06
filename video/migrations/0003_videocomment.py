# Generated by Django 2.0.4 on 2018-07-07 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0002_auto_20180707_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_modify_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='video.VideoComment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
            options={
                'verbose_name': 'comment_video',
                'verbose_name_plural': 'comment_video',
                'ordering': ['created_time'],
            },
        ),
    ]
