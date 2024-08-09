# Generated by Django 4.2.11 on 2024-08-09 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pbf', '0034_merge_20240425_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameplayer',
            name='impending',
        ),
        migrations.CreateModel(
            name='GamePlayerImpendingWithEnergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.IntegerField(default=0)),
                ('in_play', models.BooleanField(default=False)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbf.card')),
                ('gameplayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbf.gameplayer')),
            ],
            options={
                'db_table': 'pbf_gameplayer_impending_with_energy',
            },
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='impending_with_energy',
            field=models.ManyToManyField(blank=True, related_name='impending_with_energy', through='pbf.GamePlayerImpendingWithEnergy', to='pbf.card'),
        ),
    ]
