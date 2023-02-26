# Generated by Django 4.0.4 on 2022-05-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapps', '0025_filingcodes_filing_alter_applicant_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempfilingfees',
            name='filing',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='category',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Inventor', 'Inventor'), ('Individual', 'Individual')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Days', 'In Days'), ('In Years', 'In Years'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Priority Date', 'Priority Date'), ('Application Date', 'Application Date'), ('Document Date', 'Document Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Publication Date', 'PublicationDate'), ('Registration Date', 'RegistrationDate'), ('PCT Filing Date', 'PCT Filing Date'), ('Renewal Date', 'Renewal Date'), ('PCT Publication Date', 'PCT Publication Date'), ('OA Mailing Date', 'OA Mailing Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ip_matters',
            name='status',
            field=models.CharField(blank=True, choices=[('RENEWAL', 'RENEWAL'), ('REGISTERED', 'REGISTERED'), ('PENDING', 'PENDING'), ('TRANSFERRED', 'TRANSFERRED'), ('ABANDONED', 'ABANDONED'), ('CANCELLED', 'CANCELLED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Incoming', 'Incoming'), ('Others', 'Others'), ('Outgoing', 'Outgoing')], max_length=20, null=True),
        ),
    ]