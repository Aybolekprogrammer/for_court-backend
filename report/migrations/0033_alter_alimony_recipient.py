# Generated by Django 4.1.6 on 2023-06-06 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0032_alter_alimony_must_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimony',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimonies', to='report.recipient', verbose_name='Algydaryň ady we familiyasy:'),
        ),
    ]
