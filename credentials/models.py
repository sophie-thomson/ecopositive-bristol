from django.db import models
# from django.contrib.auth.models import User
# from companies.models import Company


class Credential(models.Model):
    """
    Credential model, related to 'Company'.
    A credential can be assigned to many companies, and one
    company can have multiple credentials.
    """
    name = models.CharField(max_length=40)
    group = models.CharField(max_length=40)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['group']

    def __str__(self):
        return f'{self.name}, ({self.group})'
