from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField

from model_utils import Choices

from core.indexes import GinTrigramIndex


class Perimeter(models.Model):
    """Represents a single application perimeter for an Aid.

    Each perimeter represents a location (e.g a region, a department, a
    commune…) and contains data about where it is located.

    E.g: the commune of Montpellier is located in Hérault, Occitanie, France,
    Europe.

    Since nothing is simple when administration is involved, some perimeters
    e.g epcis can be spread over several departments / regions.

    Drainage basins are another edge case, since they are independant from any
    existing legal borders.
    https://fr.wikipedia.org/wiki/Bassin_hydrographique

    """

    TYPES = Choices(
        (1, 'commune', _('Commune')),
        (5, 'epci', _('EPCI')),
        (8, 'basin', _('Drainage basin')),
        (10, 'department', _('Department')),
        (15, 'region', _('Region')),
        (20, 'country', _('Country')),
        (25, 'continent', _('Continent')),
    )

    scale = models.PositiveIntegerField(
        _('Scale'),
        choices=TYPES)
    code = models.CharField(
        _('Code'),
        max_length=16)
    name = models.CharField(
        _('Name'),
        max_length=128)

    continent = models.CharField(
        _('Continent'),
        max_length=2,
        default='EU')
    country = models.CharField(
        _('Country'),
        max_length=3,
        default='FRA')  # ISO_3166-3 codes
    regions = ArrayField(  # Array of region codes (INSEE COG)
        verbose_name=_('Regions'),
        base_field=models.CharField(max_length=2),
        default=list,
        blank=True)
    departments = ArrayField(  # Array of depts codes (INSEE COG)
        verbose_name=_('Departments'),
        base_field=models.CharField(max_length=3),
        default=list,
        blank=True)
    epci = models.CharField(
        _('EPCI'),
        max_length=32,  # INSEE COG
        blank=True)
    basin = models.CharField(
        _('Drainage basin'),
        max_length=32,  # Sandre code
        blank=True)
    zipcodes = ArrayField(
        verbose_name=_('Zip codes'),
        base_field=models.CharField(max_length=8),
        null=True, blank=True)
    is_overseas = models.BooleanField(
        verbose_name=_('Is overseas?'),
        null=True)

    class Meta:
        verbose_name = _('Perimeter')
        verbose_name_plural = _('Perimeters')
        unique_together = (
            ('scale', 'code'),
        )
        indexes = [
            GinTrigramIndex(fields=['name']),
        ]

    def __str__(self):
        if self.scale == self.TYPES.commune and self.zipcodes:
            _str = '{} ({} – {})'.format(
                self.name, self.get_scale_display(), ', '.join(self.zipcodes))
        else:
            _str = '{} ({})'.format(self.name, self.get_scale_display())

        return _str

    @property
    def id_slug(self):
        return '{}-{}'.format(self.id, slugify(self.name))
