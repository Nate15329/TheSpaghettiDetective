# Generated by Django 2.1.7 on 2019-05-18 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190323_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprinter',
            name='current_print',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app.Print'),
        ),
        migrations.AddField(
            model_name='print',
            name='alert_acknowledged_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='print',
            name='alerted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='print',
            name='ext_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='current_print',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='not_used', to='app.Print'),
        ),
    ]
