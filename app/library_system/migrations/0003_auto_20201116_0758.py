# Generated by Django 3.1.2 on 2020-11-16 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_system', '0002_menu_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('info', models.TextField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=True, verbose_name='是否在库(1:在库,0:不在库)'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_system.publisher'),
        ),
    ]