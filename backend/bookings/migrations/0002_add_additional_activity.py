# Generated migration for additional activity fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='additional_activity_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='additional_activity_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='booking',
            name='additional_activity_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
