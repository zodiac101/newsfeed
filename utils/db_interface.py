import pymongo
import traceback

#Connecting to the mongo db
def db_connect():
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")

    db_newsfeed = db_client["newsfeed"]

    collection_news = db_newsfeed['news']

    collection_news.create_index([("url", 1), ("title", 1), ("story_date", 1)], unique=True)

    return db_client, collection_news


def query_by_date(query_date, source):
    db_client, collection_news = db_connect()
    query = {'current_date': query_date, 'source': source}
    result = collection_news.count_documents(query)
    db_client.close()
    return result


def insert_records(list_news):
    try:
        db_client, collection_news = db_connect()
        result = collection_news.insert_many(list_news)
        db_client.close()
        print("{} records inserted".format(len(list_news)))
    except:
        print("Inserting duplicate records")


def query_by_date_range(start_date, end_date, source):
    db_client, collection_news = db_connect()
    query = {'current_date': {'$gte': start_date, '$lt': end_date}, 'source': source}
    result = collection_news.count_documents(query)
    db_client.close()
    return result






