# Generated by Django 4.2 on 2023-05-28 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0029_alter_alimony_must_pay_alter_alimony_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimony',
            name='executor_date',
            field=models.DateField(verbose_name='Önumçiligiň senesi:'),
        ),
        migrations.AlterField(
            model_name='alimony',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimonies', to='report.recipient', to_field='name_and_lastname', verbose_name='Algydaryň ady we familiyasy:'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='birthday',
            field=models.DateField(verbose_name='Doglan senesi:'),
        ),
    ]
