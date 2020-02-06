#!/usr/bin/python3

import requests

''' number of subscriber'''


def top_ten(subreddit):
    '''return top ten posts of subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    r = requests.get(url, headers=headers).json()
    if r.get('error') == 404:
        print('None')
        return
    el = r.get('data').get('children')
    for i, j in enumerate(el[:10], 1):
        print(j.get('data').get('title', None))
