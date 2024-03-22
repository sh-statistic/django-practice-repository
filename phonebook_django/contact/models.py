from django.db import models


# Create your models here.
class Information(models.Model):
    first_name = models.CharField(max_length=255, null=False, verbose_name='first_name', blank=False)
    last_name = models.CharField(max_length=255, null=False, verbose_name='last_name', blank=False)
    address = models.TextField(null=False, verbose_name='address', blank=False)

    class Meta:
        verbose_name = 'information'
        verbose_name_plural = 'informations'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.address}'


class Phone(models.Model):
    information = models.ForeignKey(Information, null=False, blank=False, on_delete=models.PROTECT,
                                    verbose_name='information', related_name='phons')
    phone_number = models.CharField(max_length=255, null=False, verbose_name='phone_number', blank=False)

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'

    def __str__(self):
        return self.phone_number
