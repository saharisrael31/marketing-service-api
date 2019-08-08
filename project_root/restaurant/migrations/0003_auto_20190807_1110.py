# Generated by Django 2.2.4 on 2019-08-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_restaurnat_has_private_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description_text', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='restaurnat',
            name='has_private_room',
            field=models.BooleanField(default=False),
        ),
    ]
