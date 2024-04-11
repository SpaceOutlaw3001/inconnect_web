from django.urls import path
from . import views

# пути API
urlpatterns = [
    path('', views.index, name='index'),
    path('events_page', views.events_page, name='events_page'),
    path('api/events/', views.eventsAPIView.as_view(), name='events'),
    path('api/events/<int:pk>/', views.eventsAPIView.as_view(), name='events'),
    path('api/events/detail/<int:pk>/', views.eventsDetailAPIView.as_view(), name='event'),
    path('api/images/', views.imagesAPIView.as_view(), name='images'),
    path('api/images/<int:pk>/', views.imagesDetailAPIView.as_view(), name='image'),
]


