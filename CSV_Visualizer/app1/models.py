from django.db import models

# Create your models here.
class Data(models.Model):
    title=models.TextField(max_length=250)
    file = models.FileField(upload_to='csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    