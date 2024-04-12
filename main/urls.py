from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'tags', views.TagsView, basename='tags')
router.register(r'events', views.EventsView, basename='events')
router.register(r'events/<int:pk>', views.EventsView, basename='eventsid')

# пути API
urlpatterns = [
    path('', views.index, name='index'),
    path('events_page', views.events_page, name='events_page'),
    #path('events/', views.eventsAPIView.as_view(), name='events'),
    #path('api/events/<int:pk>/', views.eventsAPIView.as_view(), name='events'),
    #path('api/events/detail/<int:pk>/', views.eventsDetailAPIView.as_view(), name='event'),
    path('api/images/', views.imagesAPIView.as_view(), name='images'),
    path('api/images/<int:pk>/', views.imagesDetailAPIView.as_view(), name='image'),

    # Пути с фильтрацией тегов и событий
    path('api/', include(router.urls)),
]


