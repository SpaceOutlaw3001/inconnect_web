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


# class eventsAPIView(APIView):
#     def get(self, request):
#         return Response(
#             {
#                 "id": 1,
#                 "title": "Идём кемпить",
#                 "text": "На природе.",
#                 "place": "леса дремучие",
#                 "date": "2024-04-20",
#                 "time": "15:00:00",
#                 "chat_link": "",
#                 "price": 100,
#                 "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#                 "tags": [
#                     "nature",
#                     "camping"
#                 ]
#             }
#         )
    
# class eventsAPIView(generics.RetrieveAPIView):
#     queryset = Event.objects.all()
#     def get(self, request):
#         queryset = self.get_queryset()
#         serializer = EventSerializer(queryset, many=True)
#         return Response(serializer.data)
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
        
        



# class imagesAPIView(generics.RetrieveAPIView):
#     queryset = Image.objects.all()
#     def get(self, request, pk):
#         queryset = self.get_queryset()
#         serializer = ImageSerializer(queryset, many=True)
#         return Response(serializer.data)
class imagesAPIView(APIView):
    def get(self, request):
        images = Image.objects.all()
        return Response({'images': ImageSerializer(images, many=True).data})
class imagesDetailAPIView(generics.RetrieveAPIView):
    # img_id = request.query_params.get('id')#request.GET.get('id', 0)
    def get(self, request, pk):
        image = Image.objects.get(pk=pk)
        return Response({'image': ImageSerializer(image).data})



@csrf_exempt
def image_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def image_detail(request, pk):
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ImageSerializer(image)
        # return JsonResponse(serializer.data)
        return JsonResponse(serializer.data['url'], safe=False)
        # return JsonResponse(serializer.data)
