import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Memoir(models.Model):
    ''' a story connection a memory dump connected to a person's season '''
    author = models.ForeignKey(
        User, verbose_name=_("Author"), null=True,
        on_delete=models.CASCADE, related_name='memoirs')
    season = models.ForeignKey(
        'Season', verbose_name=_("Season"), on_delete=models.CASCADE)
    content = models.ForeignKey(
        'ContentAtom', verbose_name=_("Content"),
        null=True, blank=True, on_delete=models.SET_NULL)
    story_audio = models.FileField(
        null=True, verbose_name=_("Story Audio"), blank=True)
    story_text = models.TextField(
        _("Story Text"), blank=True,
        help_text="context and description of the dump")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Memoir")
        verbose_name_plural = _("Memoirs")

    def get_auto_memoir(self):
        return self.objects.get(author__is_null=True)


class Season(models.Model):
    ''' a meaningful period in a life '''
    story_audio = models.FileField(_("Story Audio"), null=True, blank=True)
    story_text = models.TextField(_("Story Text"), blank=True)
    place = models.TextField(_("Place"))
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))
    biography = models.ForeignKey(
        'Biography', verbose_name=_("Biography"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Season")
        verbose_name_plural = _("Seasons")


class Biography(models.Model):
    ''' a person's life story '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: dates should be fuzzy
    date_of_birth = models.DateTimeField(
        _("Date of birth"), blank=True, null=True)
    date_of_passing = models.DateTimeField(
        _("Date of passing"), blank=True, null=True)
    place_of_birth = models.TextField(_("Place of birth"))
    place_of_passing = models.TextField(
        _("Place of passing"), blank=True, null=True)
    user = models.ForeignKey(
        User, verbose_name=_("Person"), on_delete=models.CASCADE,
        help_text='all other personal data is stored on the user')
    editors = models.ManyToManyField(User, verbose_name=_("Editors"),
        related_name='editing_bios',
        help_text='the good people that can edit this biography')
    # creator is critical when we have issues of ownership and liability
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_bios')
    is_public = models.BooleanField(_("Public"), default=False,
                    help_text='Is it public?')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Biography")
        verbose_name_plural = _("Biographies")

    @property
    def is_dead(self):
        return not self.date_of_death

    def get_absolute_url(self):
        ''' the url of the buigraphy. user the uuid for the living,
            username for the dead.
        '''
        if self.is_dead:
            return "/" + self.username
        else:
            return "/" + uuid

    def __unicode__(self):
        return 'The biography of {}'.format(self.user.get_full_name())


class ContentAtom(models.Model):
    ''' content atom '''
    owner = models.ForeignKey(
        User, verbose_name=_("Owner"), on_delete=models.CASCADE)
    placed = models.DateTimeField(_("Import date"), auto_now_add=True)
    seasons = models.ManyToManyField(
        Season, through='Memoir', related_name='memoirs')
    who = models.TextField(
        _("Who"), blank=True, help_text="who is in the atom?")
    date = models.DateTimeField(
        _("Original Date"),
        blank=True, null=True, help_text="When was this atom made?")
    image = models.ImageField(verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Content Atom")
        verbose_name_plural = _("Content Atoms")
