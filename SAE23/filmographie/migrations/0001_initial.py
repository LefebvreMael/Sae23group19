# Generated by Django 5.0.4 on 2024-05-23 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('descriptif', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=100, unique=True)),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('mot_de_passe', models.CharField(max_length=100)),
                ('type_personne', models.CharField(choices=[('PRO', 'Professionnel'), ('AMA', 'Amateur')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('annee_sortie', models.PositiveIntegerField()),
                ('affiche', models.ImageField(upload_to='affiches/')),
                ('realisateur', models.CharField(max_length=100)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films', to='filmographie.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='FilmActeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_acteurs', to='filmographie.acteur')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_acteurs', to='filmographie.film')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.PositiveIntegerField()),
                ('commentaire', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='filmographie.film')),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='filmographie.personne')),
            ],
        ),
    ]
