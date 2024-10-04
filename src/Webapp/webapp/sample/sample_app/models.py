from django.db import models
from viewflow.fields import CompositeKey

# Create your models here.
class SampleText(models.Model):
    id = CompositeKey(columns=['sample_text'])
    sample_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'sample_text'
        app_label = 'sample'
