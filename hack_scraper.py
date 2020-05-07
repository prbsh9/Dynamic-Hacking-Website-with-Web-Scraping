from bs4 import BeautifulSoup
import requests
import json
import time
data = []


def theHackerNews(x=6):
    '''Gives fresh news from internet while parameter x is in which
    you get to chose how many small headlines you want. It will get you a main
    main headline with summery, link to news and other headlines with link'''

    hackingN = requests.get('https://thehackernews.com/').text
    hackingNewsSoup = BeautifulSoup(hackingN, 'lxml')

    mainNews = hackingNewsSoup.find_all('a', class_='story-link')

    for mainN in mainNews:
        news = mainN.text.strip('\n').split('\n')
        news1_heading = news[0]

        news1_para = news[3]
        news1_a = mainN.get('href')
        data.append({'source': 'Hacker News', 'headline': news1_heading, 'summary': news1_para, 'newsLink': news1_a})


def threatPost(x=10):
    '''Gives fresh news from internet while parameter x is in which
    you get to chose how many small headlines you want. It will get you a main
    main headline with summery, link to news and other headlines with link'''

    hackingN = requests.get('https://threatpost.com/').text
    hackingNewsSoup = BeautifulSoup(hackingN, 'lxml')

    mainNews = hackingNewsSoup.find_all('article', class_='c-card')

    # # print(mainNews[0])
    # # print(len(mainNews))
    n = 0
    for mainN in mainNews:

        if mainN.p is not None:
            news1_heading = mainN.h2.a.text
            news1_a = mainN.h2.a.get('href')
            news1_para = mainN.p.text
            data.append({'source': 'threatpost', 'headline': news1_heading, 'summary': news1_para, 'newsLink': news1_a})
            # print()
            n += 1
            # print(n)
            if n > x:  # x is parameter
                break
        else:
            pass

def cyware(x=9):
    '''Gives fresh news from internet while parameter x is in which
    you get to chose how many small headlines you want. It will get you a main
    main headline with summery, link to news and other headlines with link'''

    hackingN = requests.get('https://cyware.com/cyber-security-news-articles').text
    hackingNewsSoup = BeautifulSoup(hackingN, 'lxml')

    mainNews = hackingNewsSoup.find_all('div', class_='cy-panel__body')

    # # print(mainNews[0])
    # # print(len(mainNews))
    n = 0
    for mainN in mainNews:
        news1_heading = mainN.h1.text
        news1_a = mainN.find('a', target='_blank').get('href')
        data.append({'source': 'cyware', 'headline': news1_heading, 'summary': '', 'newsLink': news1_a})

        # # print(news1_heading)
        # # print(news1_a)
        n += 1
        if n > x:  # x is parameter
            break


if __name__ == '__main__':
    while True:
        theHackerNews()
        threatPost()
        cyware()
        with open('newsHack.json', 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=1)
        time.sleep(60*60)
