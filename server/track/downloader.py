import threading

class downloader:

    callback = None

    def __init__(self, interval=1.0, path='data/', cb=None ):
        self.interval   = interval
        self.path       = path

        if cb:
            self.setCallback( cb )

        self.tick()

    def setCallback(self, cb):

        # check if it is a callback
        if hasattr( cb, '__call__' ):
            self.callback = cb

    def tick(self):

        result = self.download()
        if self.callback and result:
            self.callback( result[0], result[1] )

 #       threading.Timer( 1.0, self.tick ).start()

    def download(self):
        print "Calling download"
        return False
        return ( "/my/lol/path", "20120405_225040.json")
