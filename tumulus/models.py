import uuid

from django.db import models
from django.contrib.auth.models import User


class Tumulus(models.Model):
    ''' a person's life story '''
    # a unique key to be
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    date_of_birth = models.DateField()
    place_of_birth = models.TextField()
    date_of_death = models.DateField(blank=True, null=True)
    place_of_death = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
                                related_name='tumuli')
    editors = models.ManyToManyField(User, related_name='edits')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    @property
    def is_dead(self):
        return not self.date_of_death

    def get_absolute_url(self):
        ''' the url of the tumulus. user the uuid for the living,
            username for the dead.
        '''
        if self.is_dead:
            return "/" + self.username
        else:
            return "/" + uuid

    def __unicode__(self):
        pass


class Season(models.Model):
    ''' a meaningful period in life '''
    story_audio = models.FileField()
    story_text = models.TextField(default="")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tumulus = models.ForeignKey(Tumulus, on_delete=models.CASCADE)


class MemoryDump(models.Model):
    ''' basic content '''
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    placed = models.DateTimeField(auto_now_add=True)
    story_audio = models.FileField()
    seasons = models.ManyToManyField(Season, through='Memoir',
                                     related_name='memoirs')
    who = models.TextField(default="", help_text="who is in the dump?")
    date = models.DateField(blank=True, null=True,
                            help_text="When was this dump made?")
    image = models.ImageField()


class Memoir(models.Model):
    ''' a story connection a memory dump connected to a person's season '''
    memory_dump = models.ForeignKey('MemoryDump', on_delete=models.CASCADE)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    story = models.TextField(default="",
                             help_text="context and description of the dump")
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE,
                               related_name='memoirs')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
