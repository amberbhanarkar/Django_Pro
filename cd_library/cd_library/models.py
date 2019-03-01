from django.db import models

# Create your models here.
GENRE_CHOICES = (
		('R', 'Rock'),
		('B', 'Blues'),
		('J', 'Jazz'),
		('P', 'Pop'),
		)
	
class CD(models.Model):
	title = models.CharField(max_length=  150)
	description = models.TextField(null = False, blank = True)
	artist = models.CharField(max_length = 40)
	date = models.DateField()
	genre = models.CharField(max_length = 1, choices = GENRE_CHOICES)
	
	def __unicode__(self):
		return "%s by %s, %s" %(self.title, self.artist, self.date.year)
		