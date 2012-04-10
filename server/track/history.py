import os
import re
from datetime import datetime
import time

class history:

    jsonFiles = []

    def __init__( self, path ):
        self.loadDirectory( path )

    def loadDirectory( self, path ):
        
        # use a new list, so we can reload the directory while the server is alive
        newfiles = []

        for root, directories, files in os.walk( path ):
            for filename in files:

                result = self.parseFilename( root, filename )
                if result:
                    newfiles.append( result )

        # sort files by time
        self.jsonFiles = sorted( newfiles, key=lambda x: x[0] )


    def getNearestData( self, timestamp ):

        if not self.jsonFiles or len( self.jsonFiles ) < 2:
            return False

        if timestamp < self.jsonFiles[0][0]:
            return 0

        if timestamp > self.jsonFiles[-1][0]:
            return len(self.jsonFiles)-1

        distance = 9999999999
        nearest  = 0

        for index, ( ts, filename ) in enumerate( self.jsonFiles ):

            curDist = abs( timestamp - ts )
            if curDist < distance:
                distance = curDist
                nearest  = index

            if curDist == 0:
                break


        return nearest

    def getDataByTimestamp( self, timestamp, offset = 0 ):

        # check if index is in range
        index = self.getNearestData( timestamp )
        if not index or (index + offset) > len( self.jsonFiles ):
            return False

        (timestamp, filename ) = self.jsonFiles[ index + offset ]

        # try to open file
        handle = open( filename, 'r' )
        if handle:
            return handle.read()
        else:
            return False

    def appendByFilename( self, directory, filename ):

        result = self.parseFilename( directory, filename )
        if result:
            self.jsonFiles.append( result )


    def parseFilename( self, directory, filename ):

        # only use files in valid format
        m = re.search(r'(\d{4}\d{2}\d{2}_\d{2}\d{2}\d{2})\.json$', filename )
        if m:

            # create timestamp from filename
            dt  = datetime.strptime( m.group(1), '%Y%m%d_%H%M%S')
            key = int( time.mktime( dt.timetuple() ) )

            return ( key, directory + '/' + filename )

        else: 

            return False

