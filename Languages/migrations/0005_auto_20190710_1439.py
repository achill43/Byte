# Generated by Django 2.2 on 2019-07-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Languages', '0004_post_prortamlanguage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=55),
        ),
    ]