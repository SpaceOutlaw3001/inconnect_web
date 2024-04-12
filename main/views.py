from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event, Image, Tag
from .serializers import EventSerializer, ImageSerializer, TagSerializer
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from .service import EventFilter, TagFilter

def index(request):
    return HttpResponse(
    '''
    <h3>Привет мир!</h3>
    <h5>aaaaaaaaaaaa</h5>
    '''
        )

# просто тест, игнорируй
def events_page(request):
    events = Event.objects.all()
    images = Image.objects.all()
    return render(request, 'main/events_page.html', {'events': events, 'images': images})

# Теги с фильтрацией
class TagsView(viewsets.ModelViewSet):
    # Добавление фильтра
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    #filter_class = TagFilter
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TagFilter
    # filterset_fields = ['name']
    # Конец фильтра

    # def get(self, request):
    #      tags = Tag.objects.all()
    #      return Response({'tags': TagSerializer(tags, many=True).data})

# События с фильтрацией
class EventsView(viewsets.ModelViewSet):
    # Добавление фильтра
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter
    #filterset_fields = ['tags', 'title']
    # Конец фильтра

    # Получение списка всех событий
    def get(self, request):
        events = Event.objects.all()
        return Response({'events': EventSerializer(events, many=True).data})

    # Создание события
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'event': serializer.data})

    # Обновление события
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Ops! Primary key is not defined.'})
        try:
            instance = Event.objects.get(pk=pk)
        except:
            return Response({'error': "Couldn't find Event with the given primary key."})
        serializer = EventSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'event': serializer.data})

    # Удаление события
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Ops! Primary key is not defined.'})
        try:
            event = Event.objects.get(pk=pk)
        except:
            return Response({'error': "Couldn't find Event with the given primary key."})
        event.delete()
        return Response({'deleted_event': f'Deleted Event with id={pk}.'})

# Получение списка всех изображений
class imagesAPIView(APIView):
    def get(self, request):
        images = Image.objects.all()
        return Response({'images': ImageSerializer(images, many=True).data})

# Получение изображения по id (pk)
class imagesDetailAPIView(generics.RetrieveAPIView):
    def get(self, request, pk):
        image = Image.objects.get(pk=pk)
        return Response({'image': ImageSerializer(image).data})


# это тоже игнорь
# @csrf_exempt
# def image_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         images = Image.objects.all()
#         serializer = ImageSerializer(images, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
# @csrf_exempt
# def image_detail(request, pk):
#     try:
#         image = Image.objects.get(pk=pk)
#     except Image.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = ImageSerializer(image)
#         # return JsonResponse(serializer.data)
#         return JsonResponse(serializer.data['url'], safe=False)
#         # return JsonResponse(serializer.data)
