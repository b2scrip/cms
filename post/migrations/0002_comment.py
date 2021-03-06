# Generated by Django 2.0.4 on 2018-07-04 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_modify_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
            options={
                'ordering': ['created_time'],
                'verbose_name_plural': 'comment',
                'verbose_name': 'comment',
            },
        ),
    ]
