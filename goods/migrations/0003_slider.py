# Generated by Django 5.0.7 on 2024-11-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_remove_team_description_remove_team_facebook_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slinder_name', models.CharField(default='pending', max_length=50)),
                ('slinder_desc', models.CharField(default='pending', max_length=50)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
