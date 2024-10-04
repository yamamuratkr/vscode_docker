from django.db import models

# Create your models here.
class SampleText(models.Model):
    sample_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'sample_text'
        app_label = 'sample'
