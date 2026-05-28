from django.db import models


STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано'),
]

class Task(models.Model):
    description = models.TextField()
    detail_description = models.TextField(max_length=5000, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField(null=True, blank=True)

    def str(self):
        return f"{self.description} ({self.get_status_display()})"
