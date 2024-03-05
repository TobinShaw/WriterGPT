# Generated by Django 4.1.7 on 2024-02-26 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import postdata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
                ('single_file', models.FileField(blank=True, null=True, upload_to=postdata.models.user_directory_path)),
                ('file_uuid', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
