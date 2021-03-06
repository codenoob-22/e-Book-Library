# Generated by Django 3.0.3 on 2020-03-05 22:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.TextField(max_length=100),
        ),
    ]
