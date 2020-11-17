from django.db import models
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death =  models.DateField(blank=True, null=True)
    info = models.TextField(max_length=500, blank=True, null=True)
    motto = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Author
    fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death', 'info', 'motto')

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()