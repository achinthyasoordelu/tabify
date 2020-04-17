__author__ = 'vince'

from uguitar.ug_request import UgRequest
import urllib3

def search(arg):
    req = UgRequest()
    req.titleSearch(arg)
    return req.getUrl()
