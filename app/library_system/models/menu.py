from django.db import models
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response

class Menu(models.Model):
    title = models.CharField(max_length=50)
    parentId = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class MenuSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Menu
    fields = ('id', 'title', 'parentId', 'url', 'icon', 'sequence')

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all().order_by('sequence')