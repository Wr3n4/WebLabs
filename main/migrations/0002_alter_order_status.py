# Generated by Django 5.2 on 2025-05-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Ожидает'), ('processing', 'В обработке'), ('shipped', 'Отправлен'), ('delivered', 'Доставлен')], default='pending', max_length=20, verbose_name='Статус'),
        ),
    ]
