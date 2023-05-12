# Generated by Django 4.2 on 2023-05-12 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0012_mustpayreceipt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mustpayreceipt',
            options={'verbose_name': 'Töleg', 'verbose_name_plural': 'Tölegler'},
        ),
        migrations.AlterField(
            model_name='mustpayreceipt',
            name='alimony_percent',
            field=models.IntegerField(verbose_name='alimentiň göterimi:'),
        ),
        migrations.AlterField(
            model_name='mustpayreceipt',
            name='payment_date',
            field=models.DateField(verbose_name='Iň soňky tölenen senesi:'),
        ),
        migrations.CreateModel(
            name='Alimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='Bölüm:')),
                ('ruling', models.CharField(max_length=100, verbose_name='Karary çykaran:')),
                ('ruling_date', models.DateField(verbose_name='Kararyň senesi:')),
                ('began_paying', models.DateField(verbose_name='Alimenti töläp başlan wagty:')),
                ('ruling_scan', models.FileField(blank=True, null=True, upload_to='file/', verbose_name='Kararyň nusgasy:')),
                ('executor', models.CharField(max_length=100, verbose_name='Ýerine ýetirýän:')),
                ('executor_register', models.CharField(max_length=100, verbose_name='Önumçiligiň belgisi:')),
                ('executor_date', models.DateTimeField(verbose_name='Önumciligin senesi:')),
                ('note', models.TextField(blank=True, verbose_name='Bellik:')),
                ('status', models.BooleanField(default=False, verbose_name='Işiň statusy:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Işiň döredilen senesi:')),
                ('must_pay', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.mustpay', verbose_name='Bergidaryň ady we familiýasy:')),
                ('recipient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.recipient', verbose_name='Algydaryn ady we familiyasy:')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Admin:')),
            ],
            options={
                'verbose_name': 'Aliment',
                'verbose_name_plural': 'Alimentlar',
            },
        ),
    ]
