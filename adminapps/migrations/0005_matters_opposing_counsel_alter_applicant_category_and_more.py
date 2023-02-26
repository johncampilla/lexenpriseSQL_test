# Generated by Django 4.0.4 on 2022-04-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapps', '0004_lawyer_data_ibpchapter_lawyer_data_ibplifetimeno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matters',
            name='opposing_counsel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='category',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Inventor', 'Inventor'), ('Corporate', 'Corporate')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Document Receipt Date', 'Document Receipt Date'), ('Publication Date', 'PublicationDate'), ('Registration Date', 'RegistrationDate'), ('PCT Publication Date', 'PCT Publication Date'), ('Application Date', 'Application Date'), ('Renewal Date', 'Renewal Date'), ('Document Date', 'Document Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Priority Date', 'Priority Date'), ('OA Mailing Date', 'OA Mailing Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ip_matters',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('ABANDONED', 'ABANDONED'), ('RENEWAL', 'RENEWAL'), ('CANCELLED', 'CANCELLED'), ('TRANSFERRED', 'TRANSFERRED'), ('REGISTERED', 'REGISTERED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer_data',
            name='IBPRollNo',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer_data',
            name='Specialization',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(choices=[('Incoming', 'Incoming'), ('Others', 'Others'), ('Outgoing', 'Outgoing')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
    ]