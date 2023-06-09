# Generated by Django 4.2 on 2023-05-12 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_alter_mustpay_name_and_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='MustPayReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_assessment', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tölegiň doly möçberi:')),
                ('payment', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tölenen möçberi:')),
                ('payment_date', models.DateField(verbose_name='Tölenen senesi:')),
                ('currency', models.CharField(max_length=20, verbose_name='Walýuta:')),
                ('document_scan', models.FileField(blank=True, null=True, upload_to='file/', verbose_name='Tölegi tassyklaýan resminama:')),
                ('alimony_percent', models.IntegerField()),
                ('must_pay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.mustpay', to_field='name_and_lastname', verbose_name='Bergidar:')),
            ],
            options={
                'verbose_name': 'Toleg',
                'verbose_name_plural': 'Tolegler',
            },
        ),
    ]
