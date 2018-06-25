# Generated by Django 2.0.5 on 2018-06-14 13:20

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_examplemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExampleModel',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='文章正文'),
        ),
    ]
