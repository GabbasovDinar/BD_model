from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    def __str__(self): 
        return self.Name
        
class Project(models.Model):
    NameProject = models.CharField(max_length=100)
    Client = models.CharField(max_length=100)
    def __str__(self): 
        return self.NameProject
    
class ProjectUser(models.Model):
    UserID = models.ForeignKey('User')
    ProjectID = models.ForeignKey('Project')
    Position = models.CharField(max_length=100)
    def __str__(self): 
        return self.Position    
    
class Tasks(models.Model):
    Description = models.CharField(max_length=500) 
    ProjectID = models.ForeignKey('Project')
    ProgrammerID = models.ForeignKey('ProjectUser')
    def __str__(self): 
        return self.Description  
    
class WorkLogs(models.Model):
    DescriptionLog = models.CharField(max_length=500)
    DateLog = models.DateTimeField('date work')
    TimeWork = models.FloatField(max_length=100)
    TasksID = models.ForeignKey('Tasks')
    def __str__(self): 
            return self.DescriptionLog     
