# Generated by Django 3.2.8 on 2021-10-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_description', models.TextField()),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
