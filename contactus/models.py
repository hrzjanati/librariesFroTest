from django.db import models

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject or 'بدون موضوع'}"

    class Meta:
        verbose_name = "پیام دریافتی"
        verbose_name_plural = "پیام‌های دریافتی"