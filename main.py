# -*- coding: utf-8 -*-

import urllib2
from json import loads

def build_url(args):
    BASE_URL = 'https://api.hh.ru/vacancies'
    query = '&'.join('%s=%s' % (urllib2.quote(k), urllib2.quote(v))
                     for k,v in args.iteritems())
    return '?'.join([BASE_URL, query])


def request_page(url):
    req = urllib2.urlopen(url)
    content = req.read()
    return content


def parse_page(page):
    return loads(page)


u = build_url({
    'text': 'тестировщик'
})
r = request_page(u)
p = parse_page(r)
