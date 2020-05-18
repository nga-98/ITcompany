def user_context(request):
        is_MainManager = request.user.groups.filter(name='MainManager').exists()
        return {
            'is_MainManager': is_MainManager
        }

from .models import Client

def client_z(request):
    if request.user.is_authenticated:
        client_z=Client.objects.filter(User=request.user).exists()
        return {
                'client_z': client_z
        }
    else:
        return {

        }



