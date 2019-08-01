import gdal
from gdal import Open
from ndvi import ndvi

# Open a before image and get its only band.
before_ndvi = Open(r'x') #input desired image file name into x
before_ndvi_band = before_ndvi.GetRasterBand(1)

# Open a after image and get its only band.
after_ndvi = Open(r'y') #input desired image file name into y
after_ndvi_band = after_ndvi.GetRasterBand(1)

# Get the rows and cols from one of the images (both should always be the same)
rows, cols = before_ndvi.RasterYSize, after_ndvi.RasterXSize



# Run the function for 32-bit floating point
comparison(before_ndvi_band, after_ndvi_band, rows, cols)



print('done')
