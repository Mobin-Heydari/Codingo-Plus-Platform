from django.urls import include, path
from rest_framework import routers
from . import views




class BlogRouter(routers.DefaultRouter):

    def __init__(self):
        super().__init__()
        self.register(r'', views.BlogViewSet, basename='blog')

    def get_urls(self):
        custom_urls = [
            path('', include([
                path('', views.BlogViewSet.as_view({'get': 'list'})),
                path('create/', views.BlogViewSet.as_view({'post': 'create'})),
                path('<slug:slug>/', include([
                    # Basic detail route: GET, PUT, DELETE.
                    path('', views.BlogViewSet.as_view({
                        'get': 'retrieve',
                        'put': 'update',
                        'delete': 'destroy'
                    })),
                ])),
            ])),
        ]
        return custom_urls
    
    
class MainCategoryRouter(routers.DefaultRouter):

    def __init__(self):
        super().__init__()
        self.register(r'', views.MainCategoryViewSet, basename='blog')

    def get_urls(self):
        custom_urls = [
            path('', include([
                path('', views.MainCategoryViewSet.as_view({'get': 'list'})),
                path('create/', views.MainCategoryViewSet.as_view({'post': 'create'})),
                path('<slug:slug>/', include([
                    # Basic detail route: GET, PUT, DELETE.
                    path('', views.MainCategoryViewSet.as_view({
                        'get': 'retrieve',
                        'put': 'update',
                        'delete': 'destroy'
                    })),
                ])),
            ])),
        ]
        return custom_urls
    
    
class SubCategoryRouter(routers.DefaultRouter):

    def __init__(self):
        super().__init__()
        self.register(r'', views.SubCategoryViewSet, basename='blog')

    def get_urls(self):
        custom_urls = [
            path('', include([
                path('', views.SubCategoryViewSet.as_view({'get': 'list'})),
                path('create/', views.SubCategoryViewSet.as_view({'post': 'create'})),
                path('<slug:slug>/', include([
                    # Basic detail route: GET, PUT, DELETE.
                    path('', views.SubCategoryViewSet.as_view({
                        'get': 'retrieve',
                        'put': 'update',
                        'delete': 'destroy'
                    })),
                ])),
            ])),
        ]
        return custom_urls
    
    
class TagRouter(routers.DefaultRouter):

    def __init__(self):
        super().__init__()
        self.register(r'', views.TagViewSet, basename='blog')

    def get_urls(self):
        custom_urls = [
            path('', include([
                path('', views.TagViewSet.as_view({'get': 'list'})),
                path('create/', views.TagViewSet.as_view({'post': 'create'})),
                path('<slug:slug>/', include([
                    # Basic detail route: GET, PUT, DELETE.
                    path('', views.TagViewSet.as_view({
                        'get': 'retrieve',
                        'put': 'update',
                        'delete': 'destroy'
                    })),
                ])),
            ])),
        ]
        return custom_urls
