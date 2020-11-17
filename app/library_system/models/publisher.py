from django.db import models
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Publisher
    fields = ('name', 'info')
class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()