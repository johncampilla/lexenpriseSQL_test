# Generated by Django 4.0.4 on 2022-05-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapps', '0024_alter_applicant_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filingcodes',
            name='filing',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='category',
            field=models.CharField(choices=[('Corporate', 'Corporate'), ('Individual', 'Individual'), ('Inventor', 'Inventor')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Years', 'In Years'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Priority Date', 'Priority Date'), ('Document Date', 'Document Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Registration Date', 'RegistrationDate'), ('Publication Date', 'PublicationDate'), ('PCT Filing Date', 'PCT Filing Date'), ('Renewal Date', 'Renewal Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Application Date', 'Application Date'), ('PCT Publication Date', 'PCT Publication Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ip_matters',
            name='status',
            field=models.CharField(blank=True, choices=[('TRANSFERRED', 'TRANSFERRED'), ('RENEWAL', 'RENEWAL'), ('CANCELLED', 'CANCELLED'), ('PENDING', 'PENDING'), ('REGISTERED', 'REGISTERED'), ('ABANDONED', 'ABANDONED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mailsin',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Mail', 'Mail'), ('Personal', 'Personal'), ('Email', 'Email')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='billstatus',
            field=models.CharField(blank=True, choices=[('Billed', 'Billed'), ('Unbilled', 'Unbilled')], default='Unbilled', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Outgoing', 'Outgoing'), ('Others', 'Others'), ('Incoming', 'Incoming')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Mail', 'Mail'), ('Personal', 'Personal'), ('Email', 'Email')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
    ]