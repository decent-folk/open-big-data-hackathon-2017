import urllib2
from json import loads


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


class UdacitySiteParser(BaseSiteParser):
    def __init__(self):
        self._tmp = []

    def build_url(self):
        BASE_URL = 'https://www.udacity.com/public-api/v0/courses'
        return BASE_URL

    def request_page(self, url):
        req = urllib2.urlopen(url)
        content = req.read()
        return content

    def get_courses(self):
        page = self.request_page(self.build_url())
        self._tmp =  self._parse_page(page)['courses']

    def find_courses(self, name):
        res = []
        for course in self._tmp:
            s = course['title'].split()
            if name.lower() in course['title'].lower().split():
                res.append({'name':course['title'], 'url':course['homepage']})
        return res
