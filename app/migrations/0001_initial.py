# Generated by Django 3.1.7 on 2022-12-20 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recharge_amount', models.IntegerField()),
                ('validity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SuccessfulRecharges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recharge')),
            ],
        ),
    ]
