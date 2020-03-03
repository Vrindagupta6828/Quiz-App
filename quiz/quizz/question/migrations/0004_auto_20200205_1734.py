# Generated by Django 2.2.1 on 2020-02-05 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20200203_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=500)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]