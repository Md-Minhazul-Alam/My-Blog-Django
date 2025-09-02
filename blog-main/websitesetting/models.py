from django.db import models

# Create your models here.
class Setting(models.Model):
    site_name = models.CharField(max_length=200, default='')
    site_tagline = models.CharField(max_length=200, default='')
    site_description = models.TextField(blank=True, null=True, default='')
    site_meta_keywords = models.TextField(blank=True, null=True, default='')
    site_meta_description = models.TextField(blank=True, null=True, default='')
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    
    def __str__(self):
        return self.site_name