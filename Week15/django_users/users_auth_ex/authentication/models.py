from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=140, primary_key=True)
    password = models.CharField(max_length=140)
    
    @classmethod
    def exists(cls, email):
    	try:
    		u = cls.objects.get(email=email)
    	except cls.DoesNotExist:
    		return False

    	return True
    
    def __str__(self):
    	return self.email