from django.db import models
import datetime
from django.contrib.auth.models import User

now = datetime.datetime.now()

class product(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=now)
    votes_total = models.IntegerField(default=1)  
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    body = models.TextField(max_length=2000)
    hunter = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[0:200]
    def pub_date_pretty(self):
        return self.pub_date.strftime("%B %d, %Y") 

