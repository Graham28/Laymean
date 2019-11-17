from django.db import models

# Create your models here.
class Paper(models.Model):
  """This contains information about a paper/study"""
  title = models.CharField(max_length=500)
  objective = models.TextField(default="No abstract available")
  result = models.TextField(null=True)
  year = models.PositiveSmallIntegerField(null=True)
  link = models.CharField(max_length=500,default="laymean.com")

  def __str__(self):
   return self.title

