# Generated by Django 3.0.3 on 2020-03-11 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BookStore', '0005_auto_20200311_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalBook',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('book_title', models.TextField(max_length=100)),
                ('book_sub_title', models.TextField(blank=True, max_length=100, null=True)),
                ('isbn_number', models.TextField(blank=True, max_length=25, null=True)),
                ('book_language', models.CharField(choices=[('hindi', 'Hindi'), ('english', 'English'), ('other', 'Other')], default='hindi', max_length=40)),
                ('about_book', models.TextField(blank=True, max_length=500, null=True)),
                ('book_category', models.CharField(choices=[('textbook', 'Text book'), ('poetry', 'Poetry'), ('story', 'Story'), ('novel', 'Novel'), ('fiction', 'Fiction'), ('non_fiction', 'Non-fiction'), ('other', 'Other')], default='other', max_length=40)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('book_cover', models.TextField(max_length=100)),
                ('book_content', models.TextField(max_length=100)),
                ('author_name', models.TextField(max_length=100)),
                ('about_author', models.TextField(blank=True, max_length=500, null=True)),
                ('book_price', models.DecimalField(decimal_places=2, default=10.0, max_digits=100)),
                ('pub_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical book',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]