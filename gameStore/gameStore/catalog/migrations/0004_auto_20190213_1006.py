# Generated by Django 2.1.5 on 2019-02-13 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190210_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['video_game', 'board_game'],
            },
        ),
        migrations.AlterModelOptions(
            name='boardgameinstance',
            options={'ordering': ['board_game']},
        ),
        migrations.AlterModelOptions(
            name='videogameinstance',
            options={'ordering': ['video_game']},
        ),
        migrations.AlterField(
            model_name='boardgameinstance',
            name='condition',
            field=models.CharField(blank=True, choices=[('N', 'New'), ('U', 'Used'), ('D', 'Damaged')], default='N', help_text='Book availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='console',
            name='name',
            field=models.CharField(help_text='Enter a console (e.g. Xbox One, PC, Nintendo 64)', max_length=30),
        ),
        migrations.AlterField(
            model_name='videogameinstance',
            name='condition',
            field=models.CharField(blank=True, choices=[('N', 'New'), ('U', 'Used'), ('D', 'Damaged')], default='N', help_text='Book availability', max_length=1),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='board_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.BoardGameInstance'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='video_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.VideoGameInstance'),
        ),
    ]
