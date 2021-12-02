from django.contrib.auth.models import AbstractUser
from mainapp.models import Command
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    ROLE_USER = 'u'
    ROLE_CAPTAIN = 'c'
    ROLE_CHOICES = (
        (ROLE_USER, _('User')),
        (ROLE_CAPTAIN, _('Captain')),
    )

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    about = models.TextField(blank=True)
    role = models.CharField(_('role'), max_length=1, choices=ROLE_CHOICES, blank=False)
    telegram = models.CharField(max_length=200, blank=True)
    telegram_url = models.URLField(max_length=200, blank=True)
    command = models.ForeignKey(Command, on_delete=models.CASCADE, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.username}'

    def restore(self):
        self.is_active = True
        self.save()

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
