# Generated by Django 4.2 on 2023-04-03 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermercadosistema', '0002_alter_fornecedores_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedores', to='supermercadosistema.setores'),
        ),
    ]
