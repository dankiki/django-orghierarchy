# Generated by Django 2.2.8 on 2020-01-08 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_orghierarchy', '0007_set_editable_false_on_mptt_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_organizations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_organizations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='replaced_by',
            field=models.OneToOneField(blank=True, help_text='The organization that replaces this organization', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replaced_organization', to='django_orghierarchy.Organization'),
        ),
    ]