from django.shortcuts import render

def post_list(request):
    return render(request, 'realtime_moni/post_list.html', {})

# Create your views here.
