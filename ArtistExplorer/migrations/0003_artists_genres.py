# Generated by Django 5.0.3 on 2024-05-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtistExplorer', '0002_remove_artists_id_artists_artistid'),
    ]

    operations = [
        migrations.AddField(
            model_name='artists',
            name='Genres',
            field=models.TextField(null=True),
        ),
    ]
