# Generated by Django 3.1.3 on 2021-01-12 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Etudiant', '0005_auto_20210112_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='Cours',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Etudiant.cours'),
            preserve_default=False,
        ),
    ]
