#!/usr/bin/python3

import requests

''' number of subscriber'''


def top_ten(subreddit):
    '''return top ten posts of subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130\
            Safari/537.36"
    headers = {"User-Agent": agent}
    r = requests.get(url, headers=headers).json()
    if r.get('error') == 404:
        print('None')
        return
    el = r.get('data').get('children')
    for i, j in enumerate(el[:10], 1):
        print(j.get('data').get('title', None))
