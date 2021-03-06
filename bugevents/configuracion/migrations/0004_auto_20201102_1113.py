# Generated by Django 3.1.2 on 2020-11-02 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0003_auto_20201015_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiente',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ambiente',
            name='ubicacion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='evento',
            name='ubicacion',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='ponente',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ponente',
            name='especialidad',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ponente',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='turno',
            name='nombre',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuracion.actividad')),
            ],
        ),
    ]
