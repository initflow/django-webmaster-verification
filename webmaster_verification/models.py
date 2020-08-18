from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class VerificationCode(models.Model):

    ENGINE_CHOICES = (('bing', 'Bing'),
                      ('google', 'Google'),
                      ('majestic', 'Majestic'),
                      ('yandex', 'Yandex'),
                      ('alexa', 'Alexa'))

    engine = models.CharField('Поисковик', max_length=200, null=False, blank=False, db_index=True,
                              choices=ENGINE_CHOICES)

    code = models.CharField('Код', max_length=200, null=False, blank=False, db_index=True)