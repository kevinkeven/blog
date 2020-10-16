# Generated by Django 3.1.1 on 2020-09-23 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200923_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profile/%y/%m/%d')),
                ('bio', models.CharField(blank=True, max_length=400, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('fa_account', models.URLField(blank=True, null=True)),
                ('tw_account', models.URLField(blank=True, null=True)),
                ('in_account', models.URLField(blank=True, null=True)),
                ('li_account', models.URLField(blank=True, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]