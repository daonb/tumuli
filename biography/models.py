import uuid

from django.db import models
from django.contrib.auth.models import User


class Memoir(models.Model):
    ''' a story connection a memory dump connected to a person's season '''
    author = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='memoirs')
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    content = models.ForeignKey('ContentAtom', null=True, blank=True,
                                on_delete=models.SET_NULL)

    story_audio = models.FileField(null=True, blank=True)
    story_text = models.TextField(
        blank=True, help_text="context and description of the dump")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_auto_memoir(self):
        return self.objects.get(author__is_null=True)


class Season(models.Model):
    ''' a meaningful period in a life '''
    story_audio = models.FileField(null=True, blank=True)
    story_text = models.TextField(blank=True)
    place = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    biography = models.ForeignKey('Biography', on_delete=models.CASCADE)


class Biography(models.Model):
    ''' a person's life story '''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: dates should be fuzzy
    date_of_birth = models.DateTimeField(blank=True, null=True)
    date_of_passing = models.DateTimeField(blank=True, null=True)
    place_of_birth = models.TextField()
    place_of_passing = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
               help_text='all other personal data is stored on the user')
    editors = models.ManyToManyField(User, related_name='editing_bios',
                  help_text='the good people that can edit this biography')
    # creator is critical when we have issues of ownership and liability
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_bios')
    is_public = models.BooleanField(default=False,
                    help_text='Is it public?')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    placed = models.DateTimeField(auto_now_add=True)
    seasons = models.ManyToManyField(
        Season, through='Memoir', related_name='memoirs')
    who = models.TextField(blank=True, help_text="who is in the atom?")
    date = models.DateTimeField(
        blank=True, null=True, help_text="When was this atom made?")
    image = models.ImageField()
