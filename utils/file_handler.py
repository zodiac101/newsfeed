import pickle
import os
import datetime
import json

FILE_NAME_PICKLE = "symbols.pickle"

FILE_MODE = 0o666


def read_file_pickle():
    infile = open(FILE_NAME_PICKLE, 'rb')
    new_dict = pickle.load(infile)
    infile.close()
    return new_dict.to_dict(orient='records')


def read_file_sources(path):
    sources = []
    with open(path, "r") as openfile:
        sources.append(openfile.readline())
    openfile.close()
    return sources


def write_file_json(destination, list_news, security):
    path_dir = os.path.join(destination, str(datetime.date.today()))
    if not os.path.exists(path_dir):
        os.mkdir(path_dir, FILE_MODE)
    path_file = os.path.join(path_dir, security['symbol']+".json")
    print('writing to file: {}'.format(path_file))
    with open(path_file, 'w', encoding='utf8') as f:
        f.write(json.dumps(list_news))
    f.close()
