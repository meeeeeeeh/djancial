from django.shortcuts import render
from search.documents import UserDocument


def search(request):
    q = request.GET.get('q')

    if q:
        users_search = UserDocument.search().query("match", username=q)
    else:
        users_search = ''
    return render(request, 'friends/find-friends.html', {'users_search': users_search})
