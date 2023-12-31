# Generated by Django 3.0.5 on 2023-09-26 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonationCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=20, unique=True)),
                ('donation_date', models.DateField()),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.Donor')),
            ],
        ),
    ]
