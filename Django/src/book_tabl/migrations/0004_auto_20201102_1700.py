# Generated by Django 3.1.2 on 2020-11-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_tabl', '0003_auto_20201025_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_genres',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Жанр'),
        ),
    ]
