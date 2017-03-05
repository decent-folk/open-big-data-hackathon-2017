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
                res.append({'name':course['title'], 'url':course['homepage'], 'image':(course['image'] if 'image' in course else '')})
        return res


class GoogleSiteParser(BaseSiteParser):
    def __init__(self):
        self._tmp = []

    def __init__(self):
        self._count = 0
        self._tmp = {}

    def build_url(self, args):
        BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
        query = '&'.join('%s=%s' % (urllib2.quote(str(k)),
                         urllib2.quote(str(v))) for k, v in args.iteritems())
        return '?'.join([BASE_URL, query])

    def request_page(self, url):
        req = urllib2.urlopen(url)
        content = req.read()
        return content

    def get_book_title(self, entry):
        return entry['volumeInfo']['title'].encode('utf-8')

    def get_book_url(self, entry):
        try:
            return entry['accessInfo']['webReaderLink']
        except:
            return ''

    def get_book_img(self, entry):
        try:
            return entry['volumeInfo']['imageLinks']['thumbnail']
        except:
            return ''

    def get_all_books(self, args):
            page = self.request_page(self.build_url(args))
            return [{'title':self.get_book_title(b), 'url':self.get_book_url(b), 'image':self.get_book_img(b)} for b in self._parse_page(page)['items']]
