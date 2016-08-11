import merc
import httplib, ssl, urllib2

gm = merc.GlobalMercator()

zoom = 10

coord_meter = gm.LatLonToMeters(24.77457, 121.52369)
print coord_meter

coord_tile = gm.MetersToTile(coord_meter[0], coord_meter[1], zoom)
print coord_tile

url = 'https://rs.happyman.idv.tw/map/tw25k2001/zxy/%d_%d_%d.png'

print url % (coord_tile[0], coord_tile[1], zoom)

req = urllib2.Request(url, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
info = urllib2.urlopen(req, context=gcontext).read()
print info