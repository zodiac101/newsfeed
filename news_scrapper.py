import argparse
from itertools import repeat

from utils.file_handler import read_file_pickle, read_file_sources, write_file_json

from utils.scraper import fetch_articles

from utils.db_interface import insert_records

import nltk
import ssl
import multiprocessing


def processing_job(security, sources):
    print("scrapping security: ".format(security['symbol']))
    list_articles = fetch_articles(sources, security)
    if list_articles:
        write_file_json(path_root_dir, list_articles, security)
        insert_records(list_articles)

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')

parser = argparse.ArgumentParser(description='Run news scrapper')
parser.add_argument('--root_dir', help='Output Directory')
parser.add_argument('--source_list', help='File containing news sites')
args = parser.parse_args()

path_root_dir = args.root_dir
path_source_list = args.source_list

max_processes = multiprocessing.cpu_count() - 2

list_securities = read_file_pickle()
list_sources = read_file_sources(path_source_list)
count = 0

process_pool = multiprocessing.Pool(max_processes)

process_pool.starmap(processing_job, zip(list_securities, repeat(list_sources)))
