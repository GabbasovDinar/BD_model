# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NameProject', models.CharField(max_length=100)),
                ('Client', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Position', models.CharField(max_length=100)),
                ('ProjectID', models.ForeignKey(to='BD.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Description', models.CharField(max_length=500)),
                ('ProgrammerID', models.ForeignKey(to='BD.ProjectUser')),
                ('ProjectID', models.ForeignKey(to='BD.Project')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='WorkLogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DescriptionLog', models.CharField(max_length=500)),
                ('DateLog', models.DateTimeField(verbose_name=b'date work')),
                ('TimeWork', models.FloatField(max_length=100)),
                ('TasksID', models.ForeignKey(to='BD.Tasks')),
            ],
        ),
        migrations.AddField(
            model_name='projectuser',
            name='UserID',
            field=models.ForeignKey(to='BD.User'),
        ),
    ]
