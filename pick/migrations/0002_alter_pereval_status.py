# Generated by Django 4.2.7 on 2023-12-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pick', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval',
            name='status',
            field=models.CharField(choices=[('NEW', 'Новая информация'), ('ACCEPTED', 'Информация принята'), ('PENDING', 'В процессе'), ('REJECTED', 'Информация отклонена')], default='NEW', max_length=10),
        ),
    ]
