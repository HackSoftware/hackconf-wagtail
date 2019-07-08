from .models import HomePage, Event, NavigationItem, Speaker, Lecture
from modeltranslation.decorators import register
from wagtail_modeltranslation.translator import WagtailTranslationOptions


@register(HomePage)
class HomePageTranslationOptions(WagtailTranslationOptions):
    fields = (
        'title',
        'header_dates',
        'header_text',
        'about_text',
        'call_for_speakers_title',
        'call_for_speakers_description',
        # partners section
        'gold_partners_title',
        'silver_partners_title',
        'platinum_partners_title',
        'general_partners_title',
        'other_partners_title',
        'media_partners_title',
        'branch_partners_title',
        'old_partners_title',
        'sponsors_text',
        'sponsors_partnership_description',
        # tickets section
        'pre_register_text',
        'tickets_title',
        'tickets_description',
        # location section
        'location_title',
        'location_place',
        # fields from Page model
        'slug',
        'url_path',
        'live',
        'speakers_title',
        'workshop_speakers_title',
        'schedule_title'
    )

    required_languages = ("bg", "en")


@register(Event)
class EventTranslationOptions(WagtailTranslationOptions):
    fields = ('name', 'description')

    required_languages = ("bg", "en")


@register(NavigationItem)
class NavigationItemTranslationOptions(WagtailTranslationOptions):
    fields = ('name',)

    required_languages = ('bg', 'en')


@register(Speaker)
class SpeakerTranslationOptions(WagtailTranslationOptions):
    fields = ('name', 'description', 'rich_description', 'talk_description')


@register(Lecture)
class LectureTranslationOptions(WagtailTranslationOptions):
    fields = ('topic',)

    required_languages = ('bg', 'en')
