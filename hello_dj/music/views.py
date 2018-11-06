from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'music/music_index.html',
                  context={'str': 'LIST',
                           'format_string': '%Y年%m月%d日 %H:%M:%S',
                           'ls': [1, 2, 3],
                           'tp': ('taka', 'xiaopo', 'moran')})
