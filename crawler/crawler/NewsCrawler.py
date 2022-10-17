from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EB%86%8D%EC%97%85")
soup = BeautifulSoup(html, "html.parser")

newsList = soup.select(".news_area")
imageList = soup.select(".dsc_thumb")

for i in range(len(newsList)):
    pressNameCheck = newsList[i].select_one(".news_info").select_one(".info_group").select_one(".info").i

    if pressNameCheck is not None:
        newsList[0].select_one(".news_info").select_one(".info_group").select_one(".info").i.decompose()

    time = newsList[i].select_one(".news_info").select_one(".info_group").select(".info")[1].text
    title = newsList[i].select_one(".news_tit").text
    url = newsList[i].select_one(".news_tit").attrs["href"]
    press = newsList[i].select_one(".news_info").select_one(".info_group").select_one(".info").text
    img = imageList[i].find("img")["src"]



