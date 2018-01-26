from django.db import models
from django.db import models
from django.utils import timezone

class userDetails(models.Model):
	userName=models.CharField(max_length=40)
	password=models.CharField(max_length=40)
	
	def __str__(self):
	 return self.userName


class blogs_post(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)	
    def __str__(self):
     return self.author
