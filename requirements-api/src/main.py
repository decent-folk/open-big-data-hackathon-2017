# -*- coding: utf-8 -*-

import urllib2
from json import loads
import re
import string


def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


class PageParserException(Exception):
    pass


class BaseSiteParser:
    def _parse_page(self, page):
        return loads(page)

    def get_all_requirenments(self, args):
        raise PageParserException('No implementation')


class HeadHunterSiteParser(BaseSiteParser):
    def __init__(self):
        self._count = 0
        self._tmp = {}

    def build_url(self, args):
        BASE_URL = 'https://api.hh.ru/vacancies'
        query = '&'.join('%s=%s' % (urllib2.quote(str(k)),
                         urllib2.quote(str(v))) for k, v in args.iteritems())
        return '?'.join([BASE_URL, query])

    def request_page(self, url):
        req = urllib2.urlopen(url)
        content = req.read()
        return content

    def get_requirment(self, entry):
        try:
            return entry['snippet']['requirement'].encode('utf-8')
        except:
            return ''

    def check_page_ru(self, requirement):
        return not all(x in string.printable for x in requirement)


    def get_requirments(self, args):
        page = self.request_page(self.build_url(args))
        json = self._parse_page(page)
        for i in range(json['pages']):
            for entry in self._parse_page(self.request_page(self.build_url(
                    merge_dicts(args, {'page': i}))))['items']:
                yield self.get_requirment(entry)

    def test(self, s):
        pattern = string.ascii_letters + string.digits + string.punctuation
        return all(x in pattern for x in s) and s[0].isupper() and not s.isdigit() and not all(x in string.punctuation for x in s)

    def check(self, arr):
        self._count = self._count + 1
        for i in arr:
            self._tmp[i] = self._tmp.get(i, 0) + 1

    def get_all_requirenments(self, args):
        for r in self.get_requirments(args):
            if not self.check_page_ru(r):
                continue
            r = r.replace('</highlighttext> ', '')
            r = r.replace('</highlighttext>', '')
            r = r.replace('<highlighttext>', '')
            r = r.replace(',', ' х ')
            arr = r.split(' ')
            buf = ""
            res = []
            print r
            for s in arr:
                if s and self.test(s):
                    buf = buf + ' ' + s.strip('.)')
                    if s.endswith('.'):
                        res.append(buf)
                        buf = ""
                elif buf:
                    res.append(buf)
                    buf = ""
            if buf:
                res.append(buf)
            if res:
                self.check(res)
        return [key.strip() for key, value in self._tmp.iteritems() if value * 1.0 / self._count > 0.01]


hh = HeadHunterSiteParser()
print hh.get_all_requirenments({'text': 'Java', 'search_field':'name'})
