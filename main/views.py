from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event, Image
from .serializers import EventSerializer, ImageSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


def index(request):
    return HttpResponse(
    '''
    <h3>Привет мир!</h3>
    <h5>aaaaaaaaaaaa</h5>
    '''
        )

def events_page(request):
    events = Event.objects.all()
    images = Image.objects.all()
    return render(request, 'main/events_page.html', {'events': events, 'images': images})


class eventsAPIView(APIView):
    def get(self, request):
        events = Event.objects.all()
        return Response({'events': EventSerializer(events, many=True).data})
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'event': serializer.data})
    
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
        
        
class imagesAPIView(APIView):
    def get(self, request):
        images = Image.objects.all()
        return Response({'images': ImageSerializer(images, many=True).data})
class imagesDetailAPIView(generics.RetrieveAPIView):
    def get(self, request, pk):
        image = Image.objects.get(pk=pk)
        return Response({'image': ImageSerializer(image).data})



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
