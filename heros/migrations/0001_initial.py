# Generated by Django 5.0.6 on 2024-06-16 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('weapon', models.CharField(max_length=150)),
                ('background_story', models.TextField(blank=True)),
                ('first_ability', models.TextField(blank=True)),
                ('second_ability', models.TextField(blank=True)),
                ('third_ability', models.TextField(blank=True)),
                ('ulti', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Hero',
                'verbose_name_plural': 'Heroes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DamageDealer',
            fields=[
                ('hero_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='heros.hero')),
            ],
            options={
                'verbose_name': 'Damage Dealer',
                'verbose_name_plural': 'Damage Dealers',
                'ordering': ['name'],
            },
            bases=('heros.hero',),
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('hero_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='heros.hero')),
            ],
            options={
                'verbose_name': 'Support',
                'verbose_name_plural': 'Supports',
                'ordering': ['name'],
            },
            bases=('heros.hero',),
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('hero_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='heros.hero')),
            ],
            options={
                'verbose_name': 'Tank',
                'verbose_name_plural': 'Tanks',
                'ordering': ['name'],
            },
            bases=('heros.hero',),
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countered_hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countered_by', to='heros.hero')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counters', to='heros.hero')),
            ],
            options={
                'verbose_name': 'Counter',
                'verbose_name_plural': 'Counters',
            },
        ),
    ]
