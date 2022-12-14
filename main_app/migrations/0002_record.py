# Generated by Django 4.1.2 on 2022-10-24 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('result', models.CharField(choices=[('W', 'Win'), ('L', 'Loss')], default='W', max_length=1)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.team')),
            ],
            options={
                'ordering': ['-week'],
            },
        ),
    ]
