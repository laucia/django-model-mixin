from django.db import models
from django.utils.translation import ugettext_lazy as _


class OrderedMixin(models.Model):
    '''
    A mixin with a field that represents a relative order

    '''
    ordering = models.SmallIntegerField(
        default=1,
        verbose_name=_('ordering'),
        )

    # Verbose
    # - - - - - - - - - - - - - - - - - - - - - -
    class Meta:
        abstract = True
        ordering = ['ordering', 'pk']


class DescriptiveMixin(models.Model):
    '''
    A model with a name and an optional description

    '''
    # Fields
    # - - - - - - - - - - - - - - - - - - - - - -
    name = models.CharField(
        max_length=160,
        verbose_name=_('name'),
        )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('optional description'),
        )

    # Verbose
    # - - - - - - - - - - - - - - - - - - - - - -
    class Meta:
        abstract = True

    # Verbose
    # - - - - - - - - - - - - - - - - - - - - - -
    def __unicode__(self):
        return self.name


class ModTrackingMixin(models.Model):
    '''
    A mixin to have a model keep track of modification and creation time

    '''
    created = models.DateTimeField(
        auto_now_add=True
        )
    modified = models.DateTimeField(
        auto_now=True
        )

    class Meta:
        abstract = True
