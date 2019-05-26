from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_udemy_info():
    url = 'https://scraping-for-beginner.herokuapp.com/udemy'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    name = soup.select_one('body > div.row > div > div:nth-child(2) > div > div > div.card-image > span').string
    n_subscribers = soup.select_one(
        'body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.subscribers').string
    n_subscribers = int(n_subscribers.split('：')[1])
    n_reviews = soup.select_one(
        'body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.reviews').string
    n_reviews = int(n_reviews.split('：')[1])

    results = {
        'name': name,
        'n_subscribers': n_subscribers,
        'n_reviews': n_reviews
    }
    return results


def write_date():
    # 過去データ
    df = pd.read_csv('app/assets/data.csv')
    if datetime.strptime(df.iloc[-1]['date'], '%Y/%m/%d').date() == datetime.today().date():
        df.drop(df.index[-1], axis=0, inplace=True)

    # 新規データ
    _results = get_udemy_info()

    today_date = datetime.today().strftime('%Y/%-m/%-d')
    subscribers = _results['n_subscribers']
    reviews = _results['n_reviews']

    today_result = pd.DataFrame([[today_date, subscribers, reviews]], columns=['date', 'subscribers', 'reviews'])

    # 書き込み
    df = pd.concat([df, today_result])
    df.to_csv('app/assets/data.csv', index=False)


if __name__ == '__main__':
    write_date()
