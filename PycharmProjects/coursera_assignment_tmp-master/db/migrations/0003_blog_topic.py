# Generated by Django 2.2.6 on 2019-10-26 15:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20191026_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.User')),
                ('subscribers', models.ManyToManyField(related_name='subscriptions', to='db.User')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.User')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Blog')),
                ('likes', models.ManyToManyField(related_name='likes', to='db.User')),
            ],
        ),
    ]
