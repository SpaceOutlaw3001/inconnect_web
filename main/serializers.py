from rest_framework import routers, serializers, viewsets
from .models import Event, Image

class EventSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField('_get_img_url')
    def _get_img_url(self, obj):
        return obj.image.url

    class Meta:
        model = Event
        fields = '__all__'
    
    def create(self, validated_data):
        new_event = Event.objects.create(
            title=validated_data['title'],
            text=validated_data['text'],
            place=validated_data['place'],
            date=validated_data['date'],
            time=validated_data['time'],
            chat_link=validated_data['chat_link'],
            price=validated_data['price'],
            image = validated_data['image'],
        )
        new_event.tags.set(validated_data['tags'])
        
        return new_event
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.place = validated_data.get('place', instance.place)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.chat_link = validated_data.get('chat_link', instance.chat_link)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.tags.set(validated_data.get('tags', instance.tags))
        instance.save()

        return instance
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'