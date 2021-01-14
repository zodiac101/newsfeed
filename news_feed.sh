#!/usr/bin/env bash
python3 news_scrapper.py --root_dir="test" --source_list="site.txt"
python3 news_server.py