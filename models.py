from django.db import models

class Programmer(models.Model):
    NameProgrammer = models.CharField(max_length=100)
    EmailProgrammer = models.EmailField()
    def __str__(self): 
        return self.NameProgrammer 
    
class Manager(models.Model):
    NameManager = models.CharField(max_length=100)
    EmailManager = models.EmailField()
    def __str__(self): 
        return self.NameManager   
       
class Project(models.Model):
    NameProject = models.CharField(max_length=100)
    Client = models.CharField(max_length=100)
    
    ManagerID = models.ForeignKey('Manager')
    def __str__(self): 
        return self.NameProject
class Project_line(models.Model):
    ProjectID = models.ForeignKey('Project')
    TasksID = models.ForeignKey('Tasks')

class Tasks(models.Model):
    Description = models.CharField(max_length=100)
    TimeWork = models.FloatField(max_length=100)
    
    ProgrammerID = models.ForeignKey('Programmer')
    def __str__(self): 
        return self.Description  