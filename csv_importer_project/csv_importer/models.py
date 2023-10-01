from django.db import models

class ImportedCSV(models.Model):
    csv_file = models.FileField(upload_to='uploads/')
    # Add more fields as needed
