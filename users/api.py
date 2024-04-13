from django.http import JsonResponse
from .forms import RegisterUserForm, LoginUserForm
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
    })
    

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = RegisterUserForm({
        'username': data.get('username'),
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()
    else:
        message = 'error_xy'
    
    print(message)

    return JsonResponse({'message': message}, safe=False)