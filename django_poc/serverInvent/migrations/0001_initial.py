# Generated by Django 2.0.6 on 2018-06-26 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('server_name', models.CharField(blank=True, default='', max_length=100)),
                ('domain_name', models.CharField(blank=True, default='', max_length=100)),
                ('ip_address', models.CharField(default='0.0.0.0', max_length=100)),
                ('location', models.CharField(default='Montreal', max_length=100)),
                ('operating_system', models.CharField(choices=[('WINDOWS', 'Windows'), ('MACINTOSH', 'MAC'), ('LINUS', 'Linux')], default='WINDOWS', max_length=10)),
                ('status', models.CharField(choices=[('ONLINE', 'Online'), ('OFFLINE', 'Offline')], default='ONLINE', max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serverinvent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
