# Generated by Django 2.2.14 on 2020-08-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0007_default_focus_areas'),
    ]

    operations = [
        migrations.AddField(
            model_name='focusarea',
            name='description_de',
            field=models.TextField(help_text='Description of this area of focus. Max. 300 characters.', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='description_en',
            field=models.TextField(help_text='Description of this area of focus. Max. 300 characters.', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='description_es',
            field=models.TextField(help_text='Description of this area of focus. Max. 300 characters.', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='description_fr',
            field=models.TextField(help_text='Description of this area of focus. Max. 300 characters.', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='description_fy_NL',
            field=models.TextField(help_text='Description of this area of focus. Max. 300 characters.', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='description_nl',
            field=models.TextField(help_text='Description of this area of focus. Max. 300 characters.', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='description_pl',
            field=models.TextField(help_text='Description of this area of focus. Max. 300 characters.', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='description_pt',
            field=models.TextField(help_text='Description of this area of focus. Max. 300 characters.', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='name_de',
            field=models.CharField(help_text='The name of this area of focus. Max. 100 characters.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='name_en',
            field=models.CharField(help_text='The name of this area of focus. Max. 100 characters.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='name_es',
            field=models.CharField(help_text='The name of this area of focus. Max. 100 characters.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='name_fr',
            field=models.CharField(help_text='The name of this area of focus. Max. 100 characters.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='name_fy_NL',
            field=models.CharField(help_text='The name of this area of focus. Max. 100 characters.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='name_nl',
            field=models.CharField(help_text='The name of this area of focus. Max. 100 characters.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='name_pl',
            field=models.CharField(help_text='The name of this area of focus. Max. 100 characters.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='focusarea',
            name='name_pt',
            field=models.CharField(help_text='The name of this area of focus. Max. 100 characters.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_heading_de',
            field=models.CharField(default='Partner with us', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_heading_en',
            field=models.CharField(default='Partner with us', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_heading_es',
            field=models.CharField(default='Partner with us', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_heading_fr',
            field=models.CharField(default='Partner with us', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_heading_fy_NL',
            field=models.CharField(default='Partner with us', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_heading_nl',
            field=models.CharField(default='Partner with us', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_heading_pl',
            field=models.CharField(default='Partner with us', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_heading_pt',
            field=models.CharField(default='Partner with us', max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_intro_text_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_intro_text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_intro_text_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_intro_text_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_intro_text_fy_NL',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_intro_text_nl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_intro_text_pl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_intro_text_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_page_text_de',
            field=models.CharField(default="Let's work together", max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_page_text_en',
            field=models.CharField(default="Let's work together", max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_page_text_es',
            field=models.CharField(default="Let's work together", max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_page_text_fr',
            field=models.CharField(default="Let's work together", max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_page_text_fy_NL',
            field=models.CharField(default="Let's work together", max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_page_text_nl',
            field=models.CharField(default="Let's work together", max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_page_text_pl',
            field=models.CharField(default="Let's work together", max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='partner_page_text_pt',
            field=models.CharField(default="Let's work together", max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline_de',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline_en',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline_es',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline_fr',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline_fy_NL',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline_nl',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline_pl',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='spotlight_headline_pt',
            field=models.CharField(blank=True, help_text='Spotlight headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='take_action_title_de',
            field=models.CharField(default='Take action', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='take_action_title_en',
            field=models.CharField(default='Take action', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='take_action_title_es',
            field=models.CharField(default='Take action', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='take_action_title_fr',
            field=models.CharField(default='Take action', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='take_action_title_fy_NL',
            field=models.CharField(default='Take action', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='take_action_title_nl',
            field=models.CharField(default='Take action', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='take_action_title_pl',
            field=models.CharField(default='Take action', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='take_action_title_pt',
            field=models.CharField(default='Take action', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepagetakeactioncards',
            name='text_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepagetakeactioncards',
            name='text_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepagetakeactioncards',
            name='text_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepagetakeactioncards',
            name='text_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepagetakeactioncards',
            name='text_fy_NL',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepagetakeactioncards',
            name='text_nl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepagetakeactioncards',
            name='text_pl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepagetakeactioncards',
            name='text_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='partnerlogos',
            name='name_de',
            field=models.CharField(default='Partner Name', help_text='Alt text for the logo image.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerlogos',
            name='name_en',
            field=models.CharField(default='Partner Name', help_text='Alt text for the logo image.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerlogos',
            name='name_es',
            field=models.CharField(default='Partner Name', help_text='Alt text for the logo image.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerlogos',
            name='name_fr',
            field=models.CharField(default='Partner Name', help_text='Alt text for the logo image.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerlogos',
            name='name_fy_NL',
            field=models.CharField(default='Partner Name', help_text='Alt text for the logo image.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerlogos',
            name='name_nl',
            field=models.CharField(default='Partner Name', help_text='Alt text for the logo image.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerlogos',
            name='name_pl',
            field=models.CharField(default='Partner Name', help_text='Alt text for the logo image.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnerlogos',
            name='name_pt',
            field=models.CharField(default='Partner Name', help_text='Alt text for the logo image.', max_length=100, null=True),
        ),
    ]
