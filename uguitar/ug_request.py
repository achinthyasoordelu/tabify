__author__ = 'vince'

import urllib.parse

class UgRequest(object):
    '''
    Class to build a request for ultimate-guitar
    '''

    NETLOC = 'www.ultimate-guitar.com'
    PATH = '/search.php'
    PARAMETERS = ''
    # This should be the only one to change
    QUERY_STRING = ''
    FRAGMENT = ''
    BASE_REQUEST = ['http', NETLOC, PATH, PARAMETERS, QUERY_STRING, FRAGMENT]

    # Position of the query string in the url attributes list
    QS_POS = 4

    # http://www.ultimate-guitar.com/search.php?search_type=title&value=metallica+one

    def __init__(self):
        super(UgRequest, self).__init__()
        self._request = UgRequest.BASE_REQUEST

    def _updateQueryString(self, queryString):
        self._request[UgRequest.QS_POS] = queryString

    def titleSearch(self, searchQuery):
        '''
        Given some search keys, prepares the url tokens to search in titles
        (simplest ug search)

        :param searchQuery: search keys (e.g., "<band> <song>")
        '''
        self._request = UgRequest.BASE_REQUEST
        searchQuery = searchQuery.replace(' ', '+')
        queryString = 'search_type=title&value=' + searchQuery
        self._updateQueryString(queryString)

    def getUrl(self):
        '''
        Returns the url from the current tokens
        '''
        return urllib.parse.urlunparse(self._request)