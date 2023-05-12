from django.db import models

# Create your models here.

class director(models.Model):

    name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    img = models.ImageField(default='steven.jpg')

    def __str__(self):
        return f"{self.name} {self.last_name}"
        
    def validate(self):
        if not self.name:
            return ["The director's name is mandatory."]
        
        if not self.last_name:
            return ["The director's last name is mandatory."]
        
        return []
    
    def save(self, *args, **kwargs):
        self.validate()
        super().save(*args, **kwargs)

class movie(models.Model):

    name = models.CharField(max_length=30, null=False, blank=False)
    release_year = models.IntegerField(null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    director = models.ForeignKey(director, on_delete=models.CASCADE, null=False, blank=False)
    img = models.ImageField()

    def __str__(self):
        return f"{self.name} - {self.director.name}"
        
    def validate(self):
        if not self.name:
            return ["The movie's name is mandatory."]
        
        if not self.release_year:
            return ["The movie's release year is mandatory."]
        
        if not self.description:
            return ["The movie's description is mandatory."]
        
        if not self.director:
            return ["The director's name is mandatory."]
        
        if not self.img:
            return ["The movie's img is mandatory."]
        
        return []
    
    def save(self, *args, **kwargs):
        self.validate()
        super().save(*args, **kwargs)