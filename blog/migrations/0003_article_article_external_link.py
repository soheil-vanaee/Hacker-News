# Generated by Django 4.2 on 2023-04-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Article_External_Link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]