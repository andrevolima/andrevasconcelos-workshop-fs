# Generated by Django 4.1.7 on 2023-04-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica', '0002_remove_projetos_nome_clientes_area'),
    ]

    operations = [
        migrations.DeleteModel(
            name='projetos',
        ),
        migrations.AddField(
            model_name='clientes',
            name='projetos',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
