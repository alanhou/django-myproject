from urllib.parse import urlparse, urlunparse
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class CreationModificationDateBase:
  """
  Abstract base class with a creation and modification date and time
  """
  created = models.DateTimeField(
    _("Create Date and Time"),
    auto_now_add=True,
  )
  modified = models.DateTimeField(
    _("Modification Date and Time"),
    auto_now=True,
  )

  class Meta:
    abstract = True


class MetaTagsBase:
  """
  Abstract base class for generating meta tags
  """
  meta_keywords = models.CharField(
    _("Keywords"),
    max_length=255,
    blank=True,
    help_text=_("Separate keywords with commas.")
  )
  meta_description = models.CharField(
    _("Description"),
    max_length=255,
    blank=True,
  )
  meta_author = models.CharField(
    _("Author"),
    max_length=255,
    blank=True,
  )
  meta_copyright = models.CharField(
    _("Copyright"),
    max_length=255,
    blank=True,
  )

  class Meta:
    abstract = True

  def get_meta_field(self, name, content):
    tag = ""
    if name and content:
      tag = render_to_string("includes/meta_field.html",{
        "name": name,
        "content": content,
      })
    return mark_safe(tag)

  def get_meta_keywords(self):
    return self.get_meta_field("keywords", self.meta_keywords)

  def get_meta_description(self):
    return self.get_meta_field("description", self.meta_description)

  def get_meta_author(self):
    return self.get_meta_field("author", self.meta_author)

  def get_meta_copyright(self):
    return self.get_meta_field("copyright", self.meta_copyright)

  def get_meta_tags(self):
    return mark_safe("\n".join((
      self.get_meta_keywords(),
      self.get_meta_description(),
      self.get_meta_author(),
      self.get_meta_copyright(),
    )))


class UrlBase(models.Model):
  """
  A replacement for get_absolute_url()
  Models extending this mixin should have either get_url or get_url_path implemented.
  http://code.djangoproject.com/wiki/ReplacingGetAbsoluteUrl
  """
  class Meta:
    abstract = True

  def get_url(self):
    if(hasattr(self.get_url_path, "dont_recurse")):
      raise NotImplementedError
    try:
      path = self.get_url_path()
    except NotImplementedError:
      raise
    return settings.WEBSITE_URL + path
  get_url.dont_recurse = True

  def get_url_path(self):
    if hasattr(self.get_url, "dont_recurse"):
      raise NotImplementedError
    try:
      url = self.get_url()
    except NotImplementedError:
      raise
    bits = urlparse(url)
    return urlunparse(("", "") + bits[2:])
  get_url_path.dont_recurse = True

  def get_absolute_url(self):
    return self.get_url()