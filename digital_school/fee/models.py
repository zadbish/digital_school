from django.db import models

from django.utils import timezone

from student.models import gr_register, Classes, gardian

class fees_type(models.Model):
    fee_code = models.AutoField(primary_key=True)
    fee_type = models.CharField(max_length=255)

    class Meta:
        ordering = ('fee_code',)

    def __str__(self):
        return str(self.fee_type)

class concession_type(models.Model):
    concession_code = models.AutoField(primary_key=True)
    concession_type = models.CharField(max_length=255)
    concession_percent = models.IntegerField(default=50)

    class Meta:
        ordering = ('concession_code',)

    def __str__(self):
        return str(self.concession_type)

class fees_source(models.Model):
    source_code = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=255)

    class Meta:
        ordering = ('source_code',)

    def __str__(self):
        return str(self.source_name)

class class_fees(models.Model):
    class_code = models.ForeignKey(Classes, on_delete=models.CASCADE)
    fee_code = models.ForeignKey(fees_type, on_delete=models.CASCADE)
    fees_amount = models.BigIntegerField(default=1000)

    class Meta:
        ordering = ('class_code',)

    def __str__(self):
        return str(self.fees_amount)

class fee(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    Gr_num = models.ForeignKey(gr_register, on_delete=models.CASCADE)
    fee_code = models.ForeignKey(fees_type, on_delete=models.CASCADE)
    fee_dues = models. BigIntegerField(default=1000)
    paid_source = models.ForeignKey(fees_source, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE)
    paid = models.BooleanField(choices=BOOL_CHOICES, default=1)
    gardian_code = models.ForeignKey(gardian, on_delete=models.CASCADE, default='1')
    due_date = models.DateField(default=timezone.now)
    paid_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('Gr_num',)

    def __str__(self):
        return str(self.paid)

