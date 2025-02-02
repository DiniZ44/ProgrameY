# Generated by Django 3.1.4 on 2020-12-11 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(default='')),
                ('fundador', models.CharField(max_length=50)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Perguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeracao', models.CharField(max_length=20)),
                ('decricao', models.CharField(max_length=350)),
                ('pontuacao', models.IntegerField()),
                ('linguagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.linguagem')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letras', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=300)),
                ('letraCerta', models.BooleanField(default=False)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.perguntas')),
            ],
        ),
    ]
