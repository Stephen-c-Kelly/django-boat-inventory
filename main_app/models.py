from django.db import models
from datetime import date

# Create your models here.

CLEANING_TIME = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# Create your models here.
class Boat(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    length = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    def clean_for_today(self):
       return self.cleaning_set.filter(date=date.today()).count() >= len(CLEANING_TIME)


    def __str__(self):
        return self.make 
    
# Add new model below Boat model
class Cleaning(models.Model):
  date = models.DateField('Cleaning Date')
  cleaning_time = models.CharField('Cleaning Time',
  max_length=1,
  choices=CLEANING_TIME,
  default=CLEANING_TIME[0][0],
  )
  boat=models.ForeignKey(Boat, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_cleaning_time_display()} on {self.date}"
  class Meta:
    ordering = ['-date']
  
