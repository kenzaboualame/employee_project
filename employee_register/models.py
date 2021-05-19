from django.db import models

# Create your models here.

class Grade(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Employee(models.Model):
    matricule = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    CIN = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    Username = models.CharField(max_length=15)
    salaire = models.CharField(max_length=50)
    dateNaissance = models.CharField(max_length=20)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)