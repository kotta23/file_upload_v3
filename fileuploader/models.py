from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator

# Create your models here.
class DesignFile(models.Model):
    file = models.FileField(upload_to='designs', validators=[FileExtensionValidator(['pdf'])])
    done = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now ,blank=True )

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
