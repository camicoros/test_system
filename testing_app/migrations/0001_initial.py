# Generated by Django 4.1.5 on 2023-01-11 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(max_length=2500, verbose_name='description')),
                ('slug', models.SlugField(max_length=120, verbose_name='slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('sort_order', models.PositiveIntegerField(verbose_name='sort order')),
            ],
            options={
                'verbose_name': 'Test Set',
                'verbose_name_plural': 'Test Sets',
                'ordering': ('sort_order',),
            },
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='question')),
                ('slug', models.SlugField(max_length=120, verbose_name='slug')),
                ('several_correct_answers', models.BooleanField(default=False, verbose_name='several correct')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('sort_order', models.PositiveIntegerField(verbose_name='sort order')),
                ('test_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='testing_app.testset', verbose_name='test set')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('sort_order',),
                'unique_together': {('test_set', 'question')},
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='is correct')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('sort_order', models.PositiveIntegerField(verbose_name='sort order')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='testing_app.testquestion', verbose_name='question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ('sort_order',),
                'unique_together': {('question', 'answer')},
            },
        ),
    ]
