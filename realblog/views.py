from django.shortcuts import render

def post_list(request):
    return render(request, 'realblog/post_list.html', {})