# Generated by Django 3.2.3 on 2021-06-15 15:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('municipality', models.CharField(max_length=150)),
                ('iatacode', models.CharField(max_length=10, verbose_name='IATA Code')),
                ('airport_name', models.CharField(default='n/a', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Luggage',
            fields=[
                ('tag_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('time_stamp', models.TimeField(default=django.utils.timezone.now, verbose_name='Time Last Scanned')),
                ('origin_airport', models.CharField(max_length=150)),
                ('destination_airport', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('Checked In', 'Checked In'), ('In Transit', 'In Transit'), ('Arrived At Destination', 'Arrived At Destination'), ('Retrieved', 'Retrieved')], default='Checked In', max_length=30)),
                ('flagged', models.CharField(choices=[('N', 'N'), ('Y', 'Y')], default='N', max_length=1)),
                ('digital_signature', models.CharField(choices=[('Awaiting Signature', 'Awaiting Signature'), ('Missing', 'Missing'), ('Delayed', 'Delayed'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Awaiting Signature', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('timestamp', models.FloatField()),
                ('prevHash', models.CharField(max_length=150)),
                ('nonce', models.IntegerField(default=0)),
                ('hash_curr', models.CharField(max_length=150)),
                ('transactions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='LuggageTrackerWebApp.luggage')),
            ],
        ),
    ]
