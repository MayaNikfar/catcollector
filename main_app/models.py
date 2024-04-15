from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)


# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=256)
  color = models.CharField(max_length=20)

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})
  
  def __str__(self):
    return self.name


class Cat(models.Model):
  name = models.CharField(max_length=256)
  breed = models.CharField(max_length=256)
  description = models.TextField(max_length=256)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})
  
  def __str__(self):
    return f'{self.name} ({self.id})'

 
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  # Create a cat_id FK
  cat = models.ForeignKey(
    Cat,
    on_delete=models.CASCADE
  )

  # def fed_for_today(self):
  #   return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
    
class Meta:
    ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
      return f"Photo for cat_id: {self.cat_id} @{self.url}"