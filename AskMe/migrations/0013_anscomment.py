# Generated by Django 3.1.2 on 2020-10-27 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AskMe', '0012_auto_20201027_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('posted_by', models.CharField(default='', max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AskMe.answer')),
            ],
        ),
    ]
