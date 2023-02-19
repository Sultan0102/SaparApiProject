# Generated by Django 4.1.2 on 2023-02-19 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('availableCapacity', models.IntegerField(blank=True, db_index=True)),
            ],
            options={
                'db_table': 'Bus',
            },
        ),
        migrations.CreateModel(
            name='BusType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('capacity', models.IntegerField(blank=True, db_index=True)),
            ],
            options={
                'db_table': 'BusType',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nativeName', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'db_table': 'Language',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coordinates', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'db_table': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('totalPrice', models.IntegerField(blank=True, db_index=True)),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'db_table': 'OrderStatus',
            },
        ),
        migrations.CreateModel(
            name='PassportNumberType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('typeName', models.CharField(db_index=True, max_length=255)),
                ('format', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'db_table': 'PassportNumberType',
            },
        ),
        migrations.CreateModel(
            name='ResourceCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.TextField(db_index=True)),
            ],
            options={
                'db_table': 'ResourceCode',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.CharField(db_index=True, max_length=255)),
                ('distance', models.FloatField()),
                ('destination', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='destination', to='tickets.location')),
                ('source', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='source', to='tickets.location')),
            ],
            options={
                'db_table': 'Route',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('scheduleNumb_guide', models.IntegerField(blank=True, db_index=True)),
                ('creationDate', models.DateField(auto_now_add=True)),
                ('weekDay', models.IntegerField(blank=True, db_index=True)),
                ('beginDate', models.DateTimeField(db_index=True)),
                ('endDate', models.DateTimeField(db_index=True)),
                ('isActive', models.BooleanField(default=False)),
                ('deleteDate', models.DateTimeField(null=True)),
                ('scheduleType', models.IntegerField(blank=True, db_index=True)),
                ('bus', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.bus')),
                ('driver', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('route', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.route')),
            ],
            options={
                'db_table': 'Schedule',
            },
        ),
        migrations.CreateModel(
            name='TicketStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'db_table': 'TicketStatus',
            },
        ),
        migrations.CreateModel(
            name='TouristTrip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(blank=True, db_index=True)),
                ('deletedDate', models.DateTimeField(db_index=True, null=True)),
                ('descriptionNameCode', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='description', to='tickets.resourcecode')),
                ('guide', models.ForeignKey(blank=True, on_delete=django.db.models.fields.related.ForeignKey, related_name='Guide', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.fields.related.ForeignKey, related_name='Owner', to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.schedule')),
                ('titleNameCode', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='title', to='tickets.resourcecode')),
            ],
            options={
                'db_table': 'TouristTrip',
            },
        ),
        migrations.CreateModel(
            name='TicketPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(db_index=True, max_length=255)),
                ('lastName', models.CharField(db_index=True, max_length=255)),
                ('secondName', models.CharField(db_index=True, max_length=255)),
                ('passportNumber', models.CharField(db_index=True, max_length=255)),
                ('passportNumberType', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.passportnumbertype')),
            ],
            options={
                'db_table': 'TicketPerson',
            },
        ),
        migrations.CreateModel(
            name='ResourceValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(db_index=True, max_length=255)),
                ('language', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.language')),
                ('nameCode', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.resourcecode')),
            ],
            options={
                'db_table': 'ResourceValue',
            },
        ),
        migrations.CreateModel(
            name='PostTicket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField(blank=True, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.order')),
                ('person', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.ticketperson')),
                ('route', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='routes', to='tickets.route')),
                ('status', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.ticketstatus')),
            ],
            options={
                'db_table': 'PostTicket',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='orderStatus',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.orderstatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='schedule',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.schedule'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='location',
            name='nameCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tickets.resourcecode'),
        ),
        migrations.AddField(
            model_name='language',
            name='resourcecode',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.resourcecode'),
        ),
        migrations.AddField(
            model_name='bus',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='tickets.bustype'),
        ),
    ]
