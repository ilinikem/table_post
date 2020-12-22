from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import downloader
import requests

def index(request):
    jsonData_list = downloader.objects.all()
    count_list = downloader.objects.all().count()
    print(jsonData_list, count_list)
    paginator = Paginator(jsonData_list, 10)  # показывать по 10 записей на странице.
    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    return render(
        request,
        'index.html',
        {
         'page': page,
         'paginator': paginator,
         'count_list': count_list
         }
    )
# Create your views here.


def download_posts(request):
    downloader.objects.all().delete()
    response = requests.get('http://jsonplaceholder.typicode.com/users').json()
    response2 = requests.get('http://jsonplaceholder.typicode.com/posts').json()
    list = []
    for i in range(len(response)):
        for m in range(len(response2)):
            if response[i]['id'] == response2[m]['userId']:
                dict = {}
                dict['name'] = response[i]['name']
                dict['topic'] = response2[m]['title']
                dict['text'] = response2[m]['body']
                downloader.objects.create(name=response[i]['name'], topic=response2[m]['title'], text=response2[m]['body'])
                list.append(dict)
    return redirect('index')
