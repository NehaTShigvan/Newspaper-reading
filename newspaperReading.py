
import requests

# GET https://newsapi.org/v2/everything?q=Apple&from=2022-06-23&sortBy=popularity&apiKey=API_KEY

# curl https://newsapi.org/v2/everything -G \
#     -d q=Apple \
#     -d from=2022-06-23 \
#     -d sortBy=popularity \
#     -d apiKey=86d88277edf74fb0b82d86ccbc0749d0

'''def News():
    # query_para ={"source":"times-of-india",
    #     "sortBy":"top",
    #     "apiKey": "86d88277edf74fb0b82d86ccbc0749d0"}
    url = "https://newsapi.org/v2/articles?country=in"
    #fetching data in json format
    response = requests.get(url)#, params= query_para)
    page = response.json()
    #getting all articles in a string articles
    article = page["articles"]
    #empty list which will contain all trending news
    data = []
    
    for a in article:
        data.append(a["title"])

    for i in range(len(data)):
        print((i+1),data[i])          #printing all trending news

    speak(data)

def speak(data):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(data)

if __name__ == "__main__":
    News()      '''

#2
def speak(data):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(data)

url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=86d88277edf74fb0b82d86ccbc0749d0"
response = requests.get(url)

data = response.json()
news = data["articles"]

print("Let's start today's news session.")
for i in range(len(news)):
    
    print(news[i]["title"])
    speak(news[i]["title"])

