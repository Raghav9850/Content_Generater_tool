from django.db import models

# Create your models here.
# generator/models.py

from django.db import models

class GeneratedContent(models.Model):
    user_input = models.TextField()
    generated_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Generated Content {self.id}'
