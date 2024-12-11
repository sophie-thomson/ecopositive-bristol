from django.db import models
from django.contrib.auth.models import User
from companies.models import Company


class Endorsement(models.Model):
    """
    Endorsement model, related to 'owner' and 'company'.
    'owner' is a User that has endorsed a company.
    'endorsed' is a Company that is endorsed by an endorsement 'owner'.
    'unique_together' makes sure a user can't 'double endorse'
    the same company.
    """
    owner = models.ForeignKey(
        User, related_name='endorser', on_delete=models.CASCADE
    )
    endorsed = models.ForeignKey(
        Company, related_name='endorsed', on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company, related_name='endorsers', on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'endorsed']

    def __str__(self):
        return f'{self.owner} {self.endorsed}'