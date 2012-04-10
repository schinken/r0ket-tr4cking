from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from urlparse import parse_qs

import track

class customHTTPServer(BaseHTTPRequestHandler):

    def do_GET(self):

        params = parse_qs(self.path[2:])
        returnCode = 404
        returnStr  = ""

        if params and 'timestamp' in params:

            timestamp = int( params['timestamp'][0] )

            offset = 0
            if 'offset' in params:
                offset  = int( params['offset'][0] )

            returnStr = "%d -> %d" % ( timestamp, offset )


        self.send_response( returnCode )
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write( returnStr )
        return


def main():

    dataPath = '/home/wkr/data/eh12/data/'

    objhistory  = track.history( dataPath )
    objdownload = track.downloader( path=dataPath, cb=objhistory.appendByFilename )


    print objhistory.getDataByTimestamp( 1333971679 )


#    try:
#        server = HTTPServer(('',8080),customHTTPServer)
#        server.serve_forever()
#    except KeyboardInterrupt:
#        server.socket.close() 


if __name__ == '__main__':
    main()
