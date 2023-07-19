import feedparser
import requests
import random
from datetime import datetime

def get_weather():
    data = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&APPID=358320bdd9a0908e9b9ca86f6307eabd")
    if data.status_code == 200:
        report = random.choice(["The weather today is ",
                                "We're looking at ",
                                "Today, expect ",
                                "There's going to be ",
                                "Out and about today, you'll see "])
        weather_forecast = data.json().get('weather')
        description = weather_forecast[0].get('description')
        report += description
        main = data.json().get('main')
        temperature = main.get('temp')
        report += f". The temperature is {temperature} Celcius."
        return report, temperature
    else:
        return "There is no weather report today.", False
    
def get_news():
    news_list = []
    rss_feed = feedparser.parse('https://www.theguardian.com/uk-news/rss')
    news_list.append("Here's the news from The Guardian.")
    for i in range(3):
        news_list.append(rss_feed.entries[i].title)
    return news_list

def get_date():
    date = datetime.today()
    date_text = f"It's {date.strftime('%A')} {date.strftime('%d')} {date.strftime('%B')}."
    return date_text