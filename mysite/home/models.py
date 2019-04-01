from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index


class HomePage(Page):
    pass


@register_snippet
class Header(models.Model):
    pass


@register_snippet
class Footer(models.Model):
    pass


class OISNewsPage(Page):
    body = RichTextField()
    date = models.DateField("Post date")
    top_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    # Export fields over the API
    api_fields = [
        APIField('body'),
        APIField('top_image'),
        APIField('date'),
        APIField('related_links'),
    ]

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        InlinePanel('related_links', label="Related links"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('top_image'),
    ]
    # Parent page / subpage type rules

    # parent_page_types = ['blog.BlogIndex']
    # subpage_types = []


    # resource_panels = Page.content_panels + [
    #     InlinePanel('resource_placements', label="Resources"),
    # ]


class OISNewsPageRelatedLink(Orderable):
    page = ParentalKey(OISNewsPage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]

    api_fields = [
        APIField('name'),
        APIField('url'),
    ]
