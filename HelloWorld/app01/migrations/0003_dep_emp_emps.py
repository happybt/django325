# Generated by Django 3.2.5 on 2021-09-07 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20210906_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dep', models.CharField(max_length=32)),
                ('province', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Emps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('province', models.CharField(max_length=32)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.dep')),
            ],
        ),
    ]