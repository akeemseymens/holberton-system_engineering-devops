#!/usr/bin/python3

import requests

''' number of subscriber'''


def recurse(subreddit, hot_list=[], after=None):
    '''recurse a hotlist of subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "py3"}
    param = {'limit':100,'after':after}
    r = requests.get(url, headers=headers, params=param,
                     allow_redirects=False).json()
    after = r.get('after')
    if after is None:
        _list_title = list(map(lambda x: x.get('data').get('title'),
                               r.get('data').get('children')))
        hot_list += _list_title
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
