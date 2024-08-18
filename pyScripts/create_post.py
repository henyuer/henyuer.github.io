import os
# import pytz
from tzlocal import get_localzone
import argparse
from datetime import datetime

def create_post(title):
    # get time
    today=datetime.now(get_localzone()).strftime('%Y-%m-%d')
    date=datetime.now(get_localzone()).strftime('%Y-%m-%d %H:%M:%S %z')

    # get standard file name
    # probably Chinese could be handled
    fileName=f"{today}-{title.replace(' ','-').lower()}.md"

    # get config data of a usual post
    front_matter=f"""---
layout: post
title: "{title}"
date: {date} 
categories: []
tags: []
---
"""

    # make file
    with open(f"_posts/{fileName}",'w',encoding='utf-8') as file:
        file.write(front_matter)

    print(f"\033[33mCreate post:\033[0m \033[34m{fileName}\033[0m")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('title',type=str,help="文章标题")
    args=parser.parse_args()
    create_post(args.title)