# Generated by Django 5.0.4 on 2024-04-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('timezone', models.CharField(blank=True, max_length=100, null=True)),
                ('address_street', models.CharField(blank=True, max_length=200, null=True)),
                ('address_comment', models.CharField(blank=True, max_length=500, null=True)),
                ('full_address', models.CharField(blank=True, max_length=500, null=True)),
                ('map_position', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('website', models.CharField(blank=True, max_length=500, null=True)),
                ('mail', models.CharField(blank=True, max_length=500, null=True)),
                ('phones', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('gallery', models.CharField(blank=True, max_length=500, null=True)),
                ('category_type', models.CharField(blank=True, max_length=500, null=True)),
                ('category', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_address', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_timezone', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_address_street', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_address_comment', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_address_full_address', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_map_position', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_inn', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_type', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_subordination_name', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_subordination_timezone', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_social_groups', models.CharField(blank=True, max_length=500, null=True)),
                ('organization_id', models.CharField(blank=True, max_length=500, null=True)),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
                ('video_hostings', models.CharField(blank=True, max_length=500, null=True)),
                ('working_schedule_mon', models.CharField(blank=True, max_length=500, null=True)),
                ('working_schedule_tue', models.CharField(blank=True, max_length=500, null=True)),
                ('working_schedule_wed', models.CharField(blank=True, max_length=500, null=True)),
                ('working_schedule_thu', models.CharField(blank=True, max_length=500, null=True)),
                ('working_schedule_fri', models.CharField(blank=True, max_length=500, null=True)),
                ('working_schedule_sat', models.CharField(blank=True, max_length=500, null=True)),
                ('working_schedule_sun', models.CharField(blank=True, max_length=500, null=True)),
                ('art_type', models.CharField(blank=True, max_length=500, null=True)),
                ('audience_type', models.CharField(blank=True, max_length=500, null=True)),
                ('language', models.CharField(blank=True, max_length=500, null=True)),
                ('professional_level', models.CharField(blank=True, max_length=500, null=True)),
                ('virtual_tour', models.CharField(blank=True, max_length=500, null=True)),
                ('types', models.CharField(blank=True, max_length=500, null=True)),
                ('start', models.CharField(blank=True, max_length=500, null=True)),
                ('general_id', models.CharField(blank=True, max_length=500, null=True)),
                ('service_name', models.CharField(blank=True, max_length=500, null=True)),
                ('eipsk_id', models.CharField(blank=True, max_length=500, null=True)),
                ('culturarf', models.CharField(blank=True, max_length=500, null=True)),
                ('goscatalog_id', models.CharField(blank=True, max_length=500, null=True)),
                ('statistic', models.CharField(blank=True, max_length=500, null=True)),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'parks',
            },
        ),
    ]
