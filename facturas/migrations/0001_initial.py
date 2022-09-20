# Generated by Django 4.0.4 on 2022-09-20 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha de factura')),
                ('tipofactura', models.CharField(choices=[('Compra', 'Compra'), ('Venta', 'Venta')], max_length=10, verbose_name='Tipo de factura')),
                ('estado', models.CharField(choices=[('Abierta', 'Abierta'), ('Cerrada', 'Cerrada'), ('Anulada', 'Anulada')], default='Abierta', max_length=10, verbose_name='Estado')),
                ('rol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.rol', verbose_name='Rol')),
                ('servicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.servicio', verbose_name='Servicio')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario', verbose_name='Nombre')),
            ],
            options={
                'db_table': 'facturas_factura',
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Abierta', 'Abierta'), ('Cerrada', 'Cerrada'), ('Anulada', 'Anulada')], default='Abierta', max_length=10, verbose_name='Estado')),
                ('cantidad', models.IntegerField()),
                ('elemento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.elemento', verbose_name='elemento')),
                ('factura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='facturas.factura', verbose_name='Factura')),
            ],
        ),
    ]