from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        return {'notifications': request.user.user_notifications.filter(is_seen=False)}
    else:
        return {'notifications': []}
