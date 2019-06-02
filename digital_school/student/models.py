from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Classes(models.Model):
    class_code = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('class_code',)

    def __str__(self):
        return self.class_name


class Sections(models.Model):
    section_code = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('section_code',)

    def __str__(self):
        return self.section_name


class Area(models.Model):
    area_code = models.AutoField(primary_key=True)
    area_text = models.CharField(max_length=50, verbose_name="Area Block")

    class Meta:
        ordering = ('area_code',)

    def __str__(self):
        return self.area_text





class gr_register(models.Model):
    Gender_Choices = (
        ('M', 'Male'),
        ('FM', 'Female'),
    )
    Status_Choices = (
        ('P', 'Present'),
        ('FM', 'Left'),
    )
    gr_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_birth = models.DateField(null=True)
    classes_A = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name="classes_A", default=1, verbose_name="Class of Admission")
    sections_A = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name="sections_A", default=1, verbose_name="Section of Admission")
    gender = models.CharField(max_length=10, choices=Gender_Choices)
    classes_C = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name="classes_C", verbose_name="Current Class")
    sections_C = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name="sections_C", verbose_name="Current Section")
    address = models.CharField(max_length=100, null=True, verbose_name="Home Address")
    area_code = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area")
    status = models.CharField(max_length=10, choices=Status_Choices, default='P')

    class Meta:
        ordering = ('gr_no',)

    def __str__(self):
        return self.first_name


class session(models.Model):
    session_code = models.AutoField(primary_key=True)
    session_years = models.CharField(max_length=20)

    class Meta:
        ordering = ('session_code',)

    def __str__(self):
        return self.session_years


class class_register(models.Model):
    gr_no = models.ForeignKey(gr_register, on_delete=models.CASCADE, verbose_name="Name")
    class_code = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name="Class")
    section_code = models.ForeignKey(Sections, on_delete=models.CASCADE, verbose_name="Section")
    roll_no = models.IntegerField(null=True, verbose_name="Roll No")
    session_code = models.ForeignKey(session, on_delete=models.CASCADE, verbose_name="Session")

    class Meta:
        ordering = ('gr_no',)

    def __str__(self):
        return self.session_code


class gardian(models.Model):
    family_id = models.AutoField(primary_key=True)
    father_name = models.CharField(max_length=50 , verbose_name="Father's Name")
    gr_no = models.ForeignKey(gr_register, on_delete=models.CASCADE)
    father_profession = models.CharField(verbose_name="Father's Occupation", max_length=50)
    father_cell = models.CharField(max_length=50, verbose_name="Father's Cell Number")
    mother_name = models.CharField(max_length=50, verbose_name="Mother's Name")
    mother_cell = models.CharField(max_length=50, verbose_name="Mother's Cell Number")

    class Meta:
        ordering = ('family_id',)

    def __str__(self):
        return self.father_name