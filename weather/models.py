from django.db import models

class Measurement(models.Model):
    temp = models.FloatField()
    date_taken = models.DateTimeField()

    def __str__(self):
    	return 'temperature: {}, @{}'.format(self.temp, self.date_taken)
