# Generated by Django 4.1.1 on 2022-11-20 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField()),
                ('list_tag', models.CharField(default='none', max_length=50)),
                ('is_shared', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField()),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.template')),
            ],
        ),
        migrations.CreateModel(
            name='SharedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_user', models.CharField(max_length=200)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.list')),
            ],
        ),
        migrations.CreateModel(
            name='SharedList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_list_id', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=50, null=True)),
                ('created_on', models.DateTimeField()),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('item_text', models.CharField(max_length=100)),
                ('is_done', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField()),
                ('due_date', models.DateField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.list')),
            ],
        ),
    ]
