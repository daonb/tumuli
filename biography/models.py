import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from photologue.models import Gallery, Photo


class User(AbstractUser):
    is_editor = models.BooleanField(default=False)
    is_person = models.BooleanField(default=False)


class Person(models.Model):  # Biography
    ''' A person's life story'''
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    is_public = models.BooleanField(_("Public"),
                                    default=False,
                                    help_text=_('Is it public?'))
    modified = models.DateTimeField(auto_now=True)
    first_name = models.TextField()
    last_name = models.TextField()
    date_of_birth = models.DateTimeField(
        _("Date of birth"), blank=True, null=True)
    date_of_passing = models.DateTimeField(
        _("Date of passing"), blank=True, null=True)
    place_of_birth = models.TextField(_("Place of birth"))
    place_of_passing = models.TextField(
        _("Place of passing"), blank=True, null=True)
    editors = models.ManyToManyField(User,
                                     verbose_name=_("Editors"),
                                     related_name='editing_bios',
                                     help_text=_('the good people that can edit this biography'))
    periods = models.ManyToManyField(Period,
                                     through='periods')
    contentAtoms = models.ManyToManyField(ContentAtom,
                                          related_name='content_atoms')
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_bios')
    created = models.DateTimeField(auto_now_add=True)

        class Meta:
        verbose_name = _("Biography")
        verbose_name_plural = _("Biographies")

    @property
    def get_username(self):
        return f'{first_name}{last_name}'

    def is_dead(self):
        return not self.date_of_death

    def get_absolute_url(self):
        # Why are two options needed here?
        ''' the url of the biography. user the uuid for the living,
            username for the dead.
        '''
        if self.is_dead:
            return self.get_username()
        else:
            return "/" + uuid

    def __str__(self):
        return f'The Biography of {self.first_name}{self.last_name}'


class Period(models.Model):
    ''' a meaningful period in a life '''
    person = models.ForeignKey(
        Person, verbose_name=_("Person"), on_delete=models.CASCADE)
    title = models.CharField(
        max_length=80, help_text=_('unique title for period'))
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))
    contentAtoms = models.ManyToManyField(
        ContentAtom, related_name='content_atoms')
    place = models.TextField(_("Place"), )
    editor_notes = models.TextField(_("Comments"))

    class Meta:
        verbose_name = _("Period")
        verbose_name_plural = _("Periods")


class ContentAtom(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(
        Person, verbose_name=_("Person"), on_delete=models.CASCADE)
    # should open a dropdown list for the Person's periods
    period = models.ForeignKey(
        Period, verbose_name=_("Period"), on_delete=models.CASCADE)
    story_text = models.TextField(_("Story Text"), blank=True)
    image = models.OneToOneField(Photo, on_delete=models.CASCADE)
    gallery = models.ForeignKey(
        Gallery, null=True, blank=True, on_delete=models.SET_NULL)
    story_audio = models.FileField(_("Story Audio"), null=True, blank=True)
    added = models.DateTimeField(_("Import date"), auto_now_add=True)
    # consider creating a "Place" model
    place = models.TextField(_("Place"))
    date = models.DateTimeField(
        _("Original Date"),
        blank=True, null=True, help_text=_("When was this atom made?"))
    who = models.TextField(
        _("Who"), blank=True, help_text=_("who is in the atom?"))
    editors = models.ManyToManyField(User, verbose_name=_("Editors"),
                                     related_name='editing_bios',
                                     help_text=_('the good people that can edit this biography'))
    editor_notes = models.TextField(_("Comments"))

    class Meta:
        verbose_name = _("Content Atom")
        verbose_name_plural = _("Content Atoms")
