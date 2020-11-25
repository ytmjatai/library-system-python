from django.urls import path, include
from rest_framework import routers

from .models.menu import MenuViewSet
from .models.book import BookViewSet
from .models.category import CategoryViewSet
from .models.author import AuthorViewSet
from .models.publisher import PublisherViewSet

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet,  basename='menu')
router.register(r'book', BookViewSet,  basename='book')
router.register(r'category', CategoryViewSet,  basename='category')
router.register(r'author', AuthorViewSet,  basename='author')
router.register(r'publisher', PublisherViewSet,  basename='publisher')

urlpatterns = [
    path('', include(router.urls)),

    # 浏览器 api "登录" 按钮
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]