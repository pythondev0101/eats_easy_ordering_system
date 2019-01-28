# Generated by Django 2.1.5 on 2019-01-26 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(help_text='Enter the product description', max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the product name', max_length=50, verbose_name='Product name')),
                ('description', models.TextField(help_text='Enter the product description', max_length=1000, null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, null=True, verbose_name='Price')),
                ('active', models.BooleanField(default=True, help_text='Is active?', verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the supplier name', max_length=50, verbose_name='Supplier')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(help_text="Select the product's supplier", null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Supplier', verbose_name='Supplier'),
        ),
    ]
