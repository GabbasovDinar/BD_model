from django.db import models


class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Position = models.CharField(max_length=100)
    def __str__(self): 
        return self.Name
        
class Project(models.Model):
    NameProject = models.CharField(max_length=100)
    Client = models.CharField(max_length=100)
    #if user position manager, then
    ManagerID = models.ForeignKey('User')
    def __str__(self): 
        return self.NameProject
    
class Tasks(models.Model):
    DateWork = models.DateTimeField('date work')
    TimeWork = models.FloatField(max_length=100)
    Description = models.CharField(max_length=500)
    #if user position programmer, then
    ProgrammerID = models.ForeignKey('User')
    ProjectID = models.ForeignKey('Project')
    def __str__(self): 
        return self.Description      