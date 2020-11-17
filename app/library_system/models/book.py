from django.db import models
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response

from .author import Author
from .category import Category
from .publisher import Publisher

class Book(models.Model):

  ISBN = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
  publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True)
  summary = models.TextField(max_length=300, blank=True, null=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
  thumbnail = models.CharField(max_length=50, blank=True, null=True)
  pictures = models.CharField(max_length=50, blank=True, null=True)
  status = models.BooleanField(verbose_name="是否在库(1:在库,0:不在库)", default=True)
  
  def __str__(self):
      return self.title 

class BookSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Book
    fields = (
      'ISBN', 'title', 'author', 'summary',
      'category', 'thumbnail', 'pictures',
    )

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()