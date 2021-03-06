# Generated by Django 3.1.2 on 2020-10-19 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='作者的姓名')),
            ],
            options={
                'verbose_name_plural': 'Author',
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='出版社的名称')),
            ],
            options={
                'verbose_name_plural': 'Publisher',
                'db_table': 'Publisher',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='图书名称')),
                ('category', models.IntegerField(choices=[(1, 'Python'), (2, 'Go'), (3, 'Linux')], verbose_name='图书的类别')),
                ('pub_time', models.DateField(verbose_name='图书的出版日期')),
                ('author', models.ManyToManyField(to='api.Author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.publisher')),
            ],
            options={
                'verbose_name_plural': 'Book',
                'db_table': 'Book',
            },
        ),
    ]
