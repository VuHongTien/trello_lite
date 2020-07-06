# Generated by Django 3.0.7 on 2020-07-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('expired_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'auth_token',
            },
        ),
    ]
