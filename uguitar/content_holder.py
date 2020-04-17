__author__ = 'vince'

class ContentHolder(object):
    '''
    Utility class to store curl output.
    '''

    def __init__(self):
        super(ContentHolder, self).__init__()
        self._content = ''

    def pushContent(self, buffer):
        print("test")
        print(buffer.decode())
        self._content = self._content + buffer

    def getContent(self):
        return self._content