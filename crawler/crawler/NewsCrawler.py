from urllib.request import urlopen
from bs4 import BeautifulSoup
import MySQLdb
import mysql_auth
info = mysql_auth.info

conn = MySQLdb.connect(
    user=info['user'],
    passwd=info['passwd'],
    host=info['host'],
    db=info['db']
)

print(type(conn))
cursor = conn.cursor()
print(type(cursor))

html = urlopen("https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EB%86%8D%EC%97%85")
soup = BeautifulSoup(html, "html.parser")

result = soup.select_one(".list_news").select(".bx")
count = len(result)

newsList = list()
imageList = list()

for i in range(count):
    newsList.append(result[i].select_one(".news_area"))
    if result[i].select_one(".dsc_thumb").find("img")["src"] is None:
        imageList.append('empty')
    else:
        imageList.append(result[i].select_one(".dsc_thumb").find("img")["src"])


for i in range(count):
    pressNameCheck = newsList[i].select_one(".news_info").select_one(".info_group").select_one(".info").i

    if pressNameCheck is not None:
        newsList[0].select_one(".news_info").select_one(".info_group").select_one(".info").i.decompose()

    time = newsList[i].select_one(".news_info").select_one(".info_group").select(".info")[1].text
    title = newsList[i].select_one(".news_tit").text
    url = newsList[i].select_one(".news_tit").attrs["href"]
    press = newsList[i].select_one(".news_info").select_one(".info_group").select_one(".info").text
    img = imageList[i]
    sql = (
        "INSERT INTO sys.news2 (time,title,url,press,img) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    data = (time, title, url, press, img)
    cursor.execute(sql, data)
    # print(time, title, url, press, img)
conn.commit()
conn.close()



