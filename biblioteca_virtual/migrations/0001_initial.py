# Generated by Django 4.1.1 on 2022-11-17 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Critica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critica', models.CharField(max_length=254)),
                ('fuente', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nuevo', models.BooleanField(default=False)),
                ('leyendo', models.BooleanField(default=False)),
                ('leido', models.BooleanField(default=False)),
                ('favorito', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Resenia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('resenia', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('contrasenia', models.CharField(max_length=30)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=254)),
                ('imagen', models.CharField(max_length=120)),
                ('sinopsis', models.TextField(max_length=500)),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.autor')),
                ('critica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.critica')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.editorial')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.estado')),
                ('genero', models.ManyToManyField(to='biblioteca_virtual.genero')),
                ('resenia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.resenia')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=500)),
                ('puntuacion', models.IntegerField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.libro')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_virtual.persona'),
        ),
    ]
