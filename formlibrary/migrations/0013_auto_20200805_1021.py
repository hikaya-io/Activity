# Generated by Django 2.2.10 on 2020-08-05 17:21

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0027_auto_20200428_0711'),
        ('formlibrary', '0012_auto_20200803_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='age',
        ),
        migrations.AddField(
            model_name='household',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='household',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='household',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Creation date'),
        ),
        migrations.AddField(
            model_name='household',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='household',
            name='email',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(message='Invalid Email Address.', regex='^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$')]),
        ),
        migrations.AddField(
            model_name='household',
            name='individuals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='formlibrary.Individual'),
        ),
        migrations.AddField(
            model_name='household',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Last Modified by'),
        ),
        migrations.AddField(
            model_name='household',
            name='modified_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last Modification date'),
        ),
        migrations.AddField(
            model_name='household',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='household',
            name='prim_phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+123456789'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='household',
            name='secondary_phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+123456789'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='household',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]