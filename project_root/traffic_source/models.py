from django.db import models


Match_Types_Choices = [
    (1, "strong"),
    (2, "May Be Interested..."),
    (3, "suggetion_ilnks"),
]

class TrafficSourceModel(models.Model):
    description_text = models.CharField(max_length=200)
    creation_date = models.DateField()
    traffic_since_created = models.IntegerField(default=0)

    def __str__(self):
        return self.description_text

class TrafficSourceGroupingModel(models.Model):
    group_description = models.CharField(max_length=300)
    extra_info = models.TextField(null=True)
    match_type = models.IntegerField(choices=Match_Types_Choices)
    
    def __str__(self):
        return self.group_description

