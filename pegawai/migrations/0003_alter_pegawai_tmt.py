# Generated by Django 5.2.3 on 2025-07-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0002_pegawai_angker_2024_pegawai_golongan_pegawai_pangkat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='tmt',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='TMT'),
        ),
    ]
