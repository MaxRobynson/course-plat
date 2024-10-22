from django.db import models


class AccesRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = 'email', "Email required"
    DRAFT = 'draft', "Draft"

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMMING_SOON = 'soon', "Comming Soon"
    DRAFT = 'draft', "Draft"

class Course(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True, null=True)
    #image
    acces = models.CharField(max_length=10,
                             choices=AccesRequirement.choices,
                             default=AccesRequirement.ANYONE)
    status = models.CharField(max_length=10, 
                              choices=PublishStatus.choices, 
                              default=PublishStatus.DRAFT)
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
