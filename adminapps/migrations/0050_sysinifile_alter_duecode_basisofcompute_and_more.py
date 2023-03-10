# Generated by Django 4.0.5 on 2022-11-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapps', '0049_inifile_alter_duecode_basisofcompute_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sysinifile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Contact_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('ContactPerson', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'System INI File',
            },
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Days', 'In Days'), ('In Years', 'In Years')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Document Date', 'Document Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Publication Date', 'PublicationDate'), ('Document Receipt Date', 'Document Receipt Date'), ('Application Date', 'Application Date'), ('Priority Date', 'Priority Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Renewal Date', 'Renewal Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Registration Date', 'RegistrationDate')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ip_matters',
            name='status',
            field=models.CharField(blank=True, choices=[('REGISTERED', 'REGISTERED'), ('TRANSFERRED', 'TRANSFERRED'), ('PENDING', 'PENDING'), ('ABANDONED', 'ABANDONED'), ('RENEWAL', 'RENEWAL'), ('CANCELLED', 'CANCELLED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mailsin',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Email', 'Email'), ('Mail', 'Mail'), ('Personal', 'Personal')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='billstatus',
            field=models.CharField(blank=True, choices=[('Billed', 'Billed'), ('Unbilled', 'Unbilled')], default='Unbilled', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Outgoing', 'Outgoing'), ('Incoming', 'Incoming'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Email', 'Email'), ('Mail', 'Mail'), ('Court', 'Court'), ('Personal', 'Personal'), ('IPO', 'IPO')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
    ]
