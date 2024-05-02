from django.db import models

class ComputerModel(models.Model):
    company_name = models.CharField(max_length=40)
    model = models.CharField(max_length=60)

    memoryChoices = (
        ('64 GB', '64 GB'),
        ('128 GB','128 GB'),
        ('256 GB','256 GB'),
        ('512 GB','512 GB'),
        ('1 TB', '1 TB'),
    )
    memory = models.CharField(max_length=6, choices=memoryChoices, null=True)

    year_of_creation = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.company_name} ---> {self.model}"
