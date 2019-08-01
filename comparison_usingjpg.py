import gdal
from gdal import Open
from comparison import comparison

# Open a before image and get its only band.
before_ndvi = Open(r'officeoutside_ndvi_float32.tif') #input desired image file name into x
before_ndvi_band = before_ndvi.GetRasterBand(1)

# Open a after image and get its only band.
after_ndvi = Open(r'outsideoffice_v2_ndvi_float32.tif') #input desired image file name into y
after_ndvi_band = after_ndvi.GetRasterBand(1)

# Get the rows and cols from one of the images (both should always be the same)
rows, cols = before_ndvi.RasterYSize, before_ndvi.RasterXSize



# Run the function for 32-bit floating point
comparison(before_ndvi_band, after_ndvi_band, rows, cols)



print('done')
