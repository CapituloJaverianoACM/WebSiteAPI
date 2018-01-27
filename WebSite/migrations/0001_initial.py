# Generated by Django 2.0.1 on 2018-01-27 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('place', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ENC', 'Encargado'), ('AYU', 'Ayudante'), ('PAR', 'Participante')], max_length=10)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebSite.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('NAC', 'Maratón Nacional'), ('REG', 'Maratón Regional'), ('MUN', 'Maratón Mundial')], max_length=10)),
                ('date', models.DateField()),
                ('place', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basename', models.CharField(default='', max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('ext', models.CharField(choices=[('img', 'Image'), ('md', 'Markdown'), ('mdf', 'MarkdownForm'), ('json', 'JSON'), ('ot', 'Other')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('major', models.CharField(max_length=200)),
                ('identification', models.CharField(max_length=50, null=True)),
                ('date_major', models.DateField(null=True)),
                ('date_chapter', models.DateField(null=True)),
                ('date_birth', models.DateField(null=True)),
                ('cellphone', models.CharField(max_length=20, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('position', models.CharField(choices=[('1PRE', 'Presidente'), ('2VIC', 'Vice-Presidente'), ('3SEC', 'Secretario'), ('4TES', 'Tesorero'), ('5CM', 'Comunity Manager')], max_length=5, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('id_photo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebSite.File')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('files', models.ManyToManyField(related_name='projects', to='WebSite.File')),
                ('members', models.ManyToManyField(related_name='projects', to='WebSite.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('id_file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebSite.File')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebSite.Member')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebSite.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('files', models.ManyToManyField(related_name='tutorials', to='WebSite.File')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='teams', through='WebSite.TeamMember', to='WebSite.Member'),
        ),
        migrations.AddField(
            model_name='contest',
            name='teams',
            field=models.ManyToManyField(related_name='constests', to='WebSite.Team'),
        ),
        migrations.AddField(
            model_name='award',
            name='id_file',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebSite.File'),
        ),
        migrations.AddField(
            model_name='activitymember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebSite.Member'),
        ),
        migrations.AddField(
            model_name='activity',
            name='files',
            field=models.ManyToManyField(related_name='activities', to='WebSite.File'),
        ),
        migrations.AddField(
            model_name='activity',
            name='members',
            field=models.ManyToManyField(related_name='activities', through='WebSite.ActivityMember', to='WebSite.Member'),
        ),
    ]
