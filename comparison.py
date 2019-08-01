import numpy as np
from numpy import nan_to_num, subtract, add, divide, multiply



def comparison(in_before_band, in_after_band, in_rows, in_cols):

    """
    Performs an NDVI calculation given two input bands, as well as other information that can be retrieved from the
    original image.
    @param in_before_band A GDAL band object representing the near-infrared image data.
    @type in_before_band GDALRasterBand
    @param in_after_band A GDAL band object representing the colour image data.
    @type: in_after_band GDALRasterBand
    @param in_rows The number of rows in both input bands.
    @type: in_rows int
    @param in_cols The number of columns in both input bands.
    @type: in_cols int
    
    @return None
    """

    # Read the input bands as numpy arrays.
    before_ndvi = in_before_band.ReadAsArray(0, 0, in_cols, in_rows)
    after_ndvi = in_after_band.ReadAsArray(0, 0, in_cols, in_rows)

    # Convert the np arrays to 32-bit floating point to make sure division will occur properly.
    before_ndvi_as32 = before_ndvi.astype(np.float32)
    after_ndvi_as32 = after_ndvi.astype(np.float32)

    # comparing each rows and columns in before and after of ndvi index by subtracting only (addition will not make a diff)
    difference = subtract(before_ndvi_as32, after_ndvi_as32)
    
    
    #creating an empty numpy array
    
    y = []
    y = np.array(y)
    
    #difference == 0
    
    for element in np.nditer(difference, order = 'C'): #looping through each element in difference
      if element != 0:
        y = np.append(y,element)
        
    if y.size > 0.2*(difference.size):
      print('this place has potential environmental degradation')
    else:
      print('this place is normal')
          
    
    

    
   

   
    return None
