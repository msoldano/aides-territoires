# Generated by Django 2.1.4 on 2018-12-10 12:55

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0051_auto_20181210_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aid',
            name='aid_types',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('grant', 'Grant'), ('loan', 'Loan'), ('recoverable_advance', 'Recoverable advance'), ('interest_subsidy', 'Interest subsidy'), ('guidance', 'Guidance'), ('networking', 'Networking'), ('valorisation', 'Valorisation')], max_length=32), help_text='Specify the help type or types.', null=True, size=None, verbose_name='Aid types'),
        ),
        migrations.AlterField(
            model_name='aid',
            name='destinations',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('service', 'Service (AMO, survey)'), ('works', 'Works'), ('supply', 'Supply')], max_length=32), blank=True, null=True, size=None, verbose_name='Destinations'),
        ),
        migrations.AlterField(
            model_name='aid',
            name='mobilization_steps',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('preop', 'Preoperational'), ('op', 'Operational'), ('postop', 'Postoperation')], default='preop', max_length=32), null=True, size=None, verbose_name='Mobilization step'),
        ),
        migrations.AlterField(
            model_name='aid',
            name='targeted_audiances',
            field=core.fields.ChoiceArrayField(base_field=models.CharField(choices=[('commune', 'Commune'), ('department', 'Department'), ('region', 'Region'), ('epci', 'Audiance EPCI'), ('lessor', 'Audiance lessor'), ('association', 'Association'), ('private person', 'Private person'), ('researcher', 'Researcher')], max_length=32), null=True, size=None, verbose_name='Targeted audiances'),
        ),
    ]
