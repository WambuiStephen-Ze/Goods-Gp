# Generated by Django 5.0.7 on 2024-11-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='description',
        ),
        migrations.RemoveField(
            model_name='team',
            name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='team',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='team',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='team',
            name='position',
        ),
        migrations.RemoveField(
            model_name='team',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='team',
            name='tweeter_url',
        ),
        migrations.AddField(
            model_name='team',
            name='client1',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(default='pending', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='title',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]