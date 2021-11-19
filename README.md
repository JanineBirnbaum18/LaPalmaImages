# LaPalmaImages
Process public images from La Palma FLIR cameras

Contains:

png2gif_vulcan.py - reads images and creates a gif for each hour of data. Takes optional positional argument specified as the integer day of the month (in November), or an array of dates. If given date is 0 or argument is omitted, videos are made for all available dates:

python png2gif_vulcan.py 0 

python png2gif_vulcan.py 16

python png2gif_vulcan.py [16,17]

python png2gif_vulcan.py [16:18]


Data source:

http://vulcan1.ldeo.columbia.edu/vulcand/ldeo/raw/data/siteCv/IrCam2/PalmaImgSiteCv2021-11/
