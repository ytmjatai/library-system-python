from django.db import models
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response

class Category(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50, blank=True, null=True)
    parentId = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'title', 'code', 'parentId', 'url', 'sequence')
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('sequence')