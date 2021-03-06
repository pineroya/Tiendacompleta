# Generated by Django 3.2.12 on 2022-06-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='categoria',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='categorias',
            field=models.ManyToManyField(to='blogApp.CategoriaModel'),
        ),
        migrations.AlterField(
            model_name='categoriamodel',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
