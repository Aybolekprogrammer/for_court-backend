# Generated by Django 4.2 on 2023-05-26 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0026_mustpay_mustpay_adder_alter_alimony_executor_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimony',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Admin:'),
        ),
    ]
