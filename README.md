# r0ket-tr4cking setup

## First Steps

* clone and/or fork git repository git://github.com/Schinken/r0ket-tr4cking.git
* checkout branch "clean" (git checkout clean)
* add your new floorplans to the static/floorplans/ directory
    * change data max X/Y to the maximum values in your json file
    * change canvas max X/Y for canvas size (size of your floorplan)
    * add your floorplan names without the path to the floorFiles configuration

Optional:
* change the radar-radius (size of the radars)
* you can use offsetX and offsetY if your data is not aligned correctly


### Running on the same machine

If you install that script on the same machine where your 
json file is generated, to avoid cross-domain policy problems with the
AJAX:

* open static/main.js
** change dataURL to the path where your data is (e.g. http://r0ket.dyndns.org:8888/output.js)

### Running on a different machine

If you cant install that script on the same machine, you have to use the
php-curl-proxy in debug/proxy.php:

You need a running webserver with installed php and php5-curl extension

* change the URL in curl_init where you get your json data (debug/proxy.php)
* change the dataURL to the url "http://your.domain.tld/debug/proxy.php"

If you have php5-apc installed, the proxy caches the request for each second

## Floorplans

If you have multiple floorplans, make sure you align them in a graphics program (like gimp or sth else)
The best way to determine the coordinates of your readers, is to point with your mouse cursor
on the floorplan in your graphics program and use this coordinates (x/y)

Its always good to printout the floorplan and write down the coordinates and readerID for each reader

## Go

Just open http://your.domain.tld/ in your browser
