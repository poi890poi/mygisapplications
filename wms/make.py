from PIL import Image
import merc

gm = merc.GlobalMercator()
im = Image.open('twdtm_asterV2_30m.tif')
print im.mode
im.mode = 'I'

zoom = 10

lt = (26.0001388888889, 118.999861111111) # LatLng of left-top in GeoTIFF
rb = (20.9998611111, 123.000138889) # LatLng of right-botton in GeoTIFF
psz = 0.000277777777777778 # Pixel size of GeoTIFF, in radian
isz = (14401, 18001) # Image size of GeoTIFF, in pixels

print gm.Resolution(zoom)

imcrop = im.crop((10, 10, 20, 20))
imz10 = im.resize((int(14401 / 10), int(18001 / 10)), resample = Image.LANCZOS)

# Left-top meters, tile, pixels, bound
ltm = gm.LatLonToMeters(lt[0], lt[1])
ltt = gm.MetersToTile(ltm[0], ltm[1], zoom)
ltp = gm.MetersToPixels(ltm[0], ltm[1], zoom)
ltr = gm.PixelsToRaster(ltp[0], ltp[1], zoom)
ltbound = gm.TileLatLonBounds(ltt[0], ltt[1], zoom)
print ltm, ltt, ltr, ltbound
