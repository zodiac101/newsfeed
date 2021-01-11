import newspaper
import GoogleNews
from datetime import date



def fetch_articles(sources, security):
    articles_list = []
    google_news = GoogleNews.GoogleNews(period='1d')
    print('Finding articles for {}'.format(security['symbol']))
    google_news.search(security['symbol'])
    news_data_list = google_news.results()
    for news_data in news_data_list:
        if news_data['media'] in sources:
            article = newspaper.Article(url=news_data['link'])
            article.download()
            article.parse()
            article.nlp()
            article_dict = {
                'security': security['symbol'],
                'current_date': str(date.today()),
                'authors': article.authors,
                'story_date': article.publish_date,
                'story_time': None,
                'body': article.text,
                'title': article.title,
                'source': news_data['media'],
                'category': 'news',
                'topics': article.keywords,
                'url': article.url
            }
            articles_list.append(article_dict)
    print('Found {} articles for security {}'.format(len(articles_list), security['symbol']))
    return articles_list

