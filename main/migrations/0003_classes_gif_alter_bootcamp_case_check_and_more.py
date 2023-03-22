# Generated by Django 4.1.3 on 2022-12-04 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_topic_meme_alter_bootcamp_case_check_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='gif',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='bootcamp',
            name='case_check',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exam'),
        ),
        migrations.AlterField(
            model_name='bootcamp',
            name='case_explonation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.explonation'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.topic'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='answers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.answer'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='bootcamp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.bootcamp'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exam'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='explonation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.explonation'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='meme',
            field=models.TextField(blank=True, default='https://www.theknot.com/tk-media/images/1ee35569-83cc-4939-b510-fa12d8fe41c0~rs_768.h', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='classes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.classes'),
        ),
    ]