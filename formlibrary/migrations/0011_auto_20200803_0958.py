# Generated by Django 2.2.10 on 2020-08-03 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0027_auto_20200428_0711'),
        ('formlibrary', '0010_auto_20200714_0948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='remarks',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='individual',
            old_name='household',
            new_name='household_id',
        ),
        migrations.RenameField(
            model_name='individual',
            old_name='father_name',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='individual',
            old_name='gender',
            new_name='id_type',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='distribution',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='training',
        ),
        migrations.AddField(
            model_name='individual',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='individual',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='head_of_household',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Last Modified by'),
        ),
        migrations.AddField(
            model_name='individual',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='individual',
            name='primary_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='secondary_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.RemoveField(
            model_name='individual',
            name='program',
        ),
        migrations.AddField(
            model_name='individual',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program'),
        ),
    ]