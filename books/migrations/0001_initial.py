# Generated by Django 2.0.6 on 2018-06-19 12:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('user', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]