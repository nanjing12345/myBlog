# Generated by Django 3.1.4 on 2021-01-04 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210104_1505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('-created_at',), 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]
