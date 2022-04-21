# Generated by Django 4.0.4 on 2022-04-21 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donor', '0002_bloodrequest_blooddrive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='city',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='country',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='state',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='zipcode',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='address',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='city',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='country',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='email',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='state',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='blooddrive',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='donor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
