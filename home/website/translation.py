from .models import HomePage
from modeltranslation.decorators import register
from wagtail_modeltranslation.translator import WagtailTranslationOptions

from wagtail_modeltranslation import patch_wagtailadmin

@register(HomePage)
class HomePageTranslationOptions(WagtailTranslationOptions):
    fields = ('title', 'header_text', 'about_text', 'call_for_speakers_title', 'call_for_speakers_description',
            #sponsors section
            'gold_partners_title', 'silver_partners_title', 'platinum_partners_title',
            'general_partners_title', 'other_partners_title', 'media_partners_title',
            'branch_partners_title', 'sweet_partner_title', 'transport_partner_title',
            'sponsors_text', 'sponsors_partnership_description',
            #tickets section
            'tickets_title', 'tickets_description',
            #location section
            'location_title', 'location_place',
            #fields from Page model
            'slug', 'url_path', 'live')

    required_languages = ("bg", "en")
