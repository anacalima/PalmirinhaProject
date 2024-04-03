# Generated by Django 5.0.3 on 2024-04-03 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceitaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='grau_de_dificuldade',
            field=models.CharField(blank=True, choices=[('F', 'Fácil'), ('I', 'Intermediário'), ('D', 'Difícil')], max_length=10, null=True),
        ),
    ]
