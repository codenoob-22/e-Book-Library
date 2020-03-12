# Generated by Django 3.0.3 on 2020-03-11 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0005_auto_20200311_0432'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mylibrary', '0003_auto_20200310_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewedHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('books', models.ManyToManyField(blank=True, to='BookStore.Book')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
