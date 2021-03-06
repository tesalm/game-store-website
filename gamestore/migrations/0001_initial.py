# Generated by Django 2.0.2 on 2018-04-25 05:27

import cloudinary.models
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
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('url', models.URLField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('logo', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='logo')),
                ('banner', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='banner')),
                ('description', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='GameReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(blank=True, max_length=500)),
                ('review_star', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamestore.Game')),
            ],
        ),
        migrations.CreateModel(
            name='GameSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('ref', models.IntegerField()),
                ('pid', models.CharField(max_length=20)),
                ('price_paid', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamestore.Game')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_state', models.CharField(blank=True, default='', max_length=10000)),
                ('high_score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamestore.Game')),
            ],
        ),
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='purchasedgame',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamestore.RegUser'),
        ),
        migrations.AddField(
            model_name='gamereview',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamestore.RegUser'),
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamestore.RegUser'),
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=models.ManyToManyField(blank=True, to='gamestore.Tag'),
        ),
    ]
