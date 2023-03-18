import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import UrlParser


def get_html(url):
    response = requests.get(url)
    if response.ok:
        return response.text


def parser_text(url: str):
    q = get_html(url)
    soup = BeautifulSoup(q, 'lxml')
    w = soup.get_text().strip().lower()
    w = w.replace('\n', '  ')

    return w


def main(url: str, a):
    x = parser_text(url)
    z = []
    S = ''
    for i in range(len(x) - 1):
        S += x[i]
        if i == len(x) - 1:
            break
        if x[i] == ' ' and x[i + 1] == ' ':
            if S != '' or S != ' ':
                z.append(S.strip())
                S = ''
    while True:
        z.remove('')
        if '' not in z:
            break
    p = []
    for i in z:
        if a in i:
            p.append(i)
    try:
        if p[0] == '':
            return 'Text topilmadi'
        else:
            return p[0]
    except IndexError:
        return 'Text topilmadi'


def index(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        text = request.POST.get('text', '')
        result = main(url=url, a=text)
        if result == 'Text topilmadi':
            return render(request, 'index.html', {'result': result})
        url_obj = UrlParser(url=url, text=text, result=result)
        url_obj.save()
        return render(request, 'index.html', {'result': result})
    if request.method == 'GET':
        return render(request, 'index.html')
