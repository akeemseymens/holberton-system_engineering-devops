#!/usr/bin/python3

import requests

''' number of subscriber'''


def number_of_subscribers(subreddit):
    '''return number of subscribers'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130\
            Safari/537.36"
    headers = {"User-Agent": agent}
    r = requests.get(url, headers=headers).json().get('data')
    if r:
        return r.get('subscribers')
    return 0
