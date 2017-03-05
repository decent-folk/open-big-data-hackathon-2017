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


def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n
    current_row = range(n+1)
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


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
        page = self.request_page(self.build_url(merge_dicts({'per_page': 500},
                                                            args)))
        json = self._parse_page(page)
        for i in range(json['pages']):
            for entry in self._parse_page(self.request_page(self.build_url(
                    merge_dicts(args, {'page': i, 'per_page': 500}))))['items']:
                yield self.get_requirment(entry)

    def test(self, s):
        pattern = string.ascii_letters + string.digits + string.punctuation
        return all(x in pattern for x in s) and s[0].isupper() and not s.isdigit() and not all(x in string.punctuation for x in s)

    def check(self, arr):
        self._count = self._count + 1
        for i in arr:
            self._tmp[i] = self._tmp.get(i, 0) + 1

    def get_all_requirenments(self, args):
        prev_reqs = []
        total_count = 0
        for r in self.get_requirments(args):
            if not self.check_page_ru(r):
                continue
            if r in prev_reqs:
                continue
            else:
                prev_reqs.append(r)
                total_count += 1
            r = r.replace('(', ' х ')
            r = r.replace(')', ' х ')
            r = r.replace('</highlighttext> ', '')
            r = r.replace('</highlighttext>', '')
            r = r.replace('<highlighttext>', '')
            r = r.replace(',', ' х ')
            r = r.replace('/', ' х ')
            r = r.replace('\\', ' х ')
            arr = r.split(' ')
            buf = ""
            res = []
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
        res0 = {key.strip(): value for key, value in self._tmp.items()}
        for word in res0.keys():
            for phrase in res0.keys():
                if word == phrase:
                    continue
                if word in phrase.split():
                    res0[phrase] += res0[word]
                    del res0[word]
                    break
        res = {}
        for i in res0.keys():
            fl = True
            for j in res.keys():
                d = distance(i.lower(), j.lower())
                if d <= min(len(i) // 3, len(j) // 3):
                    fl = False
                    res[j] += res0[i]
                    break
            if fl:
                res[i] = res0[i]
        return sorted([(k, 1.0 * v / total_count) for k, v in res.iteritems()
                       if 1.0 * v / total_count > 0.02],
                      key=lambda x: x[1], reverse=True)
