# Generated by Django 2.2.14 on 2020-09-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0001_to_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='blurb_de',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='blurb_en',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='blurb_es',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='blurb_fr',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='blurb_fy_NL',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='blurb_nl',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='blurb_pl',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='blurb_pt',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_de',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_en',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_es',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_fr',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_fy_NL',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_nl',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_pl',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='company_pt',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_vulnerabilities_helptext_de',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_vulnerabilities_helptext_en',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_vulnerabilities_helptext_es',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_vulnerabilities_helptext_fr',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_vulnerabilities_helptext_fy_NL',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_vulnerabilities_helptext_nl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_vulnerabilities_helptext_pl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manage_vulnerabilities_helptext_pt',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_de',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_es',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_fr',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_fy_NL',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_nl',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_pl',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_pt',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_helptext_de',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_helptext_en',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_helptext_es',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_helptext_fr',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_helptext_fy_NL',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_helptext_nl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_helptext_pl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy_helptext_pt',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_helptext_de',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_helptext_en',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_helptext_es',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_helptext_fr',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_helptext_fy_NL',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_helptext_nl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_helptext_pl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='security_updates_helptext_pt',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strong_password_helptext_de',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strong_password_helptext_en',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strong_password_helptext_es',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strong_password_helptext_fr',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strong_password_helptext_fy_NL',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strong_password_helptext_nl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strong_password_helptext_pl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='strong_password_helptext_pt',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_helptext_de',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_helptext_en',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_helptext_es',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_helptext_fr',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_helptext_fy_NL',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_helptext_nl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_helptext_pl',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uses_encryption_helptext_pt',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
