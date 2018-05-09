from __future__ import unicode_literals
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel


class HomePage(Page):
    # header section
    header_image_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    live_stream = models.CharField(max_length=255, blank=True, null=True)
    header_dates = models.CharField(max_length=255, blank=True, null=True)
    header_text = models.CharField(max_length=255, blank=True, null=True)
    # navigation section
    # about section
    video_id = models.CharField(max_length=255, blank=True, null=True)
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    about_text = RichTextField(blank=True, null=True)
    # speakers section
    # TODO: add fields for this section

    # call for speakers section
    show_call_for_speakers_section = models.BooleanField(default=True)
    call_for_speakers_title = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    call_for_speakers_form_url = models.URLField(max_length=255, blank=True, null=True)
    call_for_speakers_description = RichTextField(blank=True, null=True)
    call_for_speakers_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # schedule section
    show_schedule = models.BooleanField(default=False)
    schedule_title = models.CharField(max_length=50, blank=True, null=True)

    # speackers section
    show_speakers_section = models.BooleanField(default=False)
    speakers_title = models.CharField(max_length=50, blank=True, null=True)

    # sponsors section
    show_sponsors_section = models.BooleanField(default=False)
    sponsors_text = RichTextField(blank=True, null=True)
    attendees_text = RichTextField(blank=True, null=True)
    streaming_text = RichTextField(blank=True, null=True)
    fb_text = RichTextField(blank=True, null=True)
    show_sponsorship_document = models.BooleanField(default=False)
    sponsors_partnership_description = RichTextField(blank=True, null=True)
    sponsors_partnership_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    show_general_partners = models.BooleanField(default=True)
    show_platinum_partners = models.BooleanField(default=True)
    show_gold_partners = models.BooleanField(default=True)
    show_silver_partners = models.BooleanField(default=True)
    show_other_partners = models.BooleanField(default=True)
    show_media_partners = models.BooleanField(default=True)
    show_branch_partners = models.BooleanField(default=True)

    general_partners_title = models.CharField(max_length=50, null=True, blank=True)
    platinum_partners_title = models.CharField(max_length=50, null=True, blank=True)
    gold_partners_title = models.CharField(max_length=50, null=True, blank=True)
    silver_partners_title = models.CharField(max_length=50, null=True, blank=True)
    other_partners_title = models.CharField(max_length=50, null=True, blank=True)
    media_partners_title = models.CharField(max_length=50, null=True, blank=True)
    branch_partners_title = models.CharField(max_length=50, null=True, blank=True)

    # past events section

    show_pre_register = models.BooleanField(default=False)
    pre_register_text = RichTextField(blank=True, null=True)
    pre_register_url = models.URLField(max_length=255, blank=True, null=True)

    # tickets section
    show_tickets = models.BooleanField(default=True)
    tickets_title = models.CharField(max_length=255, blank=True, null=True)
    tickets_description = RichTextField(blank=True, null=True)
    tickets_widget_code = models.TextField(blank=True, null=True)

    # location section
    location_title = models.CharField(max_length=255, blank=True, null=True)
    location_place = models.CharField(max_length=255, blank=True, null=True)
    location_contact = models.CharField(max_length=255, blank=True, null=True)
    location_time = models.CharField(max_length=255, blank=True, null=True)
    footer_organized_by = models.ForeignKey(
        'website.Partner',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    footer_powered_by = models.ForeignKey(
        'website.Partner',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    footer_code_of_conduct_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    footer_terms_and_conditions_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    footer_privacy_policy_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('header_dates'),
        ImageChooserPanel('header_image_logo'),
        FieldPanel('live_stream'),
        FieldPanel('header_text'),
        FieldPanel('video_id'),
        ImageChooserPanel('about_image'),
        FieldPanel('about_text'),

        InlinePanel('navigation_items', label="Navigation items"),

        FieldPanel('show_call_for_speakers_section'),
        FieldPanel('call_for_speakers_title'),
        FieldPanel('call_for_speakers_form_url'),
        FieldPanel('call_for_speakers_description'),
        ImageChooserPanel('call_for_speakers_image'),

        FieldPanel('show_schedule'),
        FieldPanel('schedule_title'),
        InlinePanel('schedule_day_one', label="Day One Lectures"),
        InlinePanel('schedule_day_two', label="Day Two Lectures"),
        InlinePanel('workshops_day_one', label="Day One Workshops"),
        InlinePanel('workshops_day_two', label="Day Two Workshops"),

        FieldPanel('show_speakers_section'),
        FieldPanel('speakers_title'),
        InlinePanel('speakers_info', label="Speakers Info"),

        FieldPanel('sponsors_text'),
        FieldPanel('attendees_text'),
        FieldPanel('streaming_text'),
        FieldPanel('fb_text'),
        FieldPanel('show_sponsorship_document'),
        FieldPanel('sponsors_partnership_description'),
        DocumentChooserPanel('sponsors_partnership_document'),
        FieldPanel('show_sponsors_section'),
        FieldPanel('general_partners_title'),
        FieldPanel('show_general_partners'),
        InlinePanel('general_partners', label="General Partners"),
        FieldPanel('platinum_partners_title'),
        FieldPanel('show_platinum_partners'),
        InlinePanel('platinum_partners', label="Platinum Partners"),
        FieldPanel('gold_partners_title'),
        FieldPanel('show_gold_partners'),
        InlinePanel('gold_partners', label="Gold Partners"),
        FieldPanel('silver_partners_title'),
        FieldPanel('show_silver_partners'),
        InlinePanel('silver_partners', label="Silver Partners"),
        FieldPanel('other_partners_title'),
        FieldPanel('show_other_partners'),
        InlinePanel('other_partners', label="Other Partners"),
        FieldPanel('media_partners_title'),
        FieldPanel('show_media_partners'),
        InlinePanel('media_partners', label="Media Partners"),
        FieldPanel('branch_partners_title'),
        FieldPanel('show_branch_partners'),
        InlinePanel('branch_partners', label="Branch Partners"),

        InlinePanel('past_events', label="Past Events"),

        FieldPanel('show_pre_register'),
        FieldPanel('pre_register_text'),
        FieldPanel('pre_register_url'),
        FieldPanel('show_tickets'),
        FieldPanel('tickets_title'),
        FieldPanel('tickets_description'),
        FieldPanel('tickets_widget_code'),
        FieldPanel('location_title'),
        FieldPanel('location_place'),
        FieldPanel('location_contact'),
        FieldPanel('location_time'),
        SnippetChooserPanel('footer_organized_by'),
        InlinePanel('hosting_partners', label="Hosting Partners"),
        SnippetChooserPanel('footer_powered_by'),
        DocumentChooserPanel('footer_code_of_conduct_document'),
        DocumentChooserPanel('footer_terms_and_conditions_document'),
        DocumentChooserPanel('footer_privacy_policy_document'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('slug'),
    ]


@register_snippet
class Lecture(models.Model):
    topic = models.CharField(max_length=255)
    speaker = models.ForeignKey('website.Speaker', related_name='+', null=True, blank=True)
    start_time = models.DateTimeField()

    panels = [
        FieldPanel('topic'),
        FieldPanel('speaker'),
        FieldPanel('start_time')
    ]

    def __str__(self):
        return self.topic


@register_snippet
class Workshop(models.Model):
    topic = models.CharField(max_length=255)
    lector = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    enroll_url = models.URLField(max_length=255, blank=True, null=True)

    panels = [
        FieldPanel('topic'),
        FieldPanel('lector'),
        FieldPanel('start_time'),
        FieldPanel('enroll_url')
    ]

    def __str__(self):
        return self.topic


class ScheduleDayOne(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='schedule_day_one')
    lecture = models.ForeignKey('website.Lecture', related_name='+')

    panels = [
        SnippetChooserPanel('lecture'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.lecture.topic)


class ScheduleDayTwo(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='schedule_day_two')
    lecture = models.ForeignKey('website.Lecture', related_name='+')

    panels = [
        SnippetChooserPanel('lecture'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.lecture.topic)


class WorkshopsDayOne(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='workshops_day_one')
    workshop = models.ForeignKey('website.Workshop', related_name='+')

    panels = [
        SnippetChooserPanel('workshop'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.workshop.topic)


class WorkshopsDayTwo(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='workshops_day_two')
    workshop = models.ForeignKey('website.Workshop', related_name='+')

    panels = [
        SnippetChooserPanel('workshop'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.workshop.topic)


@register_snippet
class Speaker(models.Model):
    name = models.CharField(max_length=255)
    video_url = models.URLField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    rich_description = RichTextField(blank=True, null=True)
    talk_description = RichTextField(blank=True, null=True)
    picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('video_url'),
        FieldPanel('description'),
        FieldPanel('rich_description'),
        FieldPanel('talk_description'),
        ImageChooserPanel('picture'),
    ]

    def __str__(self):
        return self.name


class SpeakersInfo(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='speakers_info')
    speaker = models.ForeignKey('website.Speaker', related_name='+')

    panels = [
        SnippetChooserPanel('speaker'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.speaker.name)


@register_snippet
class Partner(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    website_url = models.URLField(max_length=255, blank=True, null=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('logo'),
        FieldPanel('website_url'),
    ]

    def __str__(self):
        return self.name


class GeneralPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='general_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class PlatinumPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='platinum_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class GoldPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='gold_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class SilverPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='silver_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class OtherPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='other_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class MediaPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='media_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class BranchPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='branch_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


class HostingPartners(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='hosting_partners')
    partner = models.ForeignKey('website.Partner', related_name='+')

    panels = [
        SnippetChooserPanel('partner'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)


@register_snippet
class NavigationItem(Orderable, models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    redirect_to = models.CharField(max_length=40, blank=True, null=True)

    content_panels = [
        FieldPanel('name'),
        FieldPanel('redirect_to'),
    ]

    def __str__(self):
        return self.name


class NavigationItems(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='navigation_items')
    navigation_item = models.ForeignKey('website.NavigationItem', related_name='+')

    panels = [
        SnippetChooserPanel('navigation_item'),
    ]


@register_snippet
class Event(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    video_id = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    content_panels = [
        FieldPanel('name'),
        FieldPanel('video_id'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.name


class PastEvents(Orderable, models.Model):
    page = ParentalKey('website.HomePage', related_name='past_events')
    event = models.ForeignKey('website.Event', related_name='+')

    panels = [
        SnippetChooserPanel('event'),
    ]

    def __str__(self):
        return "{} -> {}".format(self.page.title, self.partner.name)
