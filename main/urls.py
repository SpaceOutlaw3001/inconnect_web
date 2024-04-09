from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events_page', views.events_page, name='events_page'),
    path('api/events', views.eventsAPIView.as_view(), name='events'),
    path('api/events/<int:pk>', views.eventsAPIView.as_view(), name='events'),
    path('api/images', views.imagesAPIView.as_view(), name='images'),
    path('api/images/<int:pk>', views.imagesDetailAPIView.as_view(), name='image'),
    path('api/image_test/<int:pk>', views.image_detail),
]


