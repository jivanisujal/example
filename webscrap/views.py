from django.shortcuts import render
import requests
import bs4
# Create your views here.
def home(request):
    values = []
    if request.method == "POST":
        web_url = request.POST['url']
        resp = requests.get(web_url)
        scrapData = bs4.BeautifulSoup(resp.text,'html.parser')
        # print(scrapData.find_all('h3'))
        print(scrapData.head.title)
        for data in scrapData.find_all('h3'):
            values.append(data.text)
        #     # img_url = data.get('src')
        #     print(data.text)
    return render(request,'demo.html',{'data':values})