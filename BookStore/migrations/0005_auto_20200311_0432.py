# Generated by Django 3.0.3 on 2020-03-10 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0004_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='about_author',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='about_book',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_category',
            field=models.CharField(choices=[('textbook', 'Text book'), ('poetry', 'Poetry'), ('story', 'Story'), ('novel', 'Novel'), ('fiction', 'Fiction'), ('non_fiction', 'Non-fiction'), ('other', 'Other')], default='other', max_length=40),
        ),
        migrations.AddField(
            model_name='book',
            name='book_language',
            field=models.CharField(choices=[('hindi', 'Hindi'), ('english', 'English'), ('other', 'Other')], default='hindi', max_length=40),
        ),
        migrations.AddField(
            model_name='book',
            name='book_sub_title',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn_number',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
    ]
