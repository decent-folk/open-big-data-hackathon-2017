# -*- coding: utf-8 -*-

import urllib2
from json import loads


def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def build_url(args):
    BASE_URL = 'https://api.hh.ru/vacancies'
    query = '&'.join('%s=%s' % (urllib2.quote(str(k)), urllib2.quote(str(v)))
                     for k,v in args.iteritems())
    return '?'.join([BASE_URL, query])


def request_page(url):
    req = urllib2.urlopen(url)
    content = req.read()
    return content


def parse_page(page):
    return loads(page)


def get_requirments(entry):
    try:
        return entry['snippet']['requirement'].encode('utf-8')
    except:
        return ''


def get_all_requirments(args):
    page = request_page(build_url(args))
    json = parse_page(page)
    for i in range(json['pages']):
        for entry in parse_page(request_page(build_url(
                merge_dicts(args, {'page': i}))))['items']:
            yield get_requirments(entry)


for i in get_all_requirments({'text': 'тестировщик'}):
    print i


# u = build_url({'text': 'тестировщик'})
# r = request_page(u)
# p = parse_page(r)
# print get_requirments(p)
